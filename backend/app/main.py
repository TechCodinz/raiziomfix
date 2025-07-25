
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .models import User, Transaction
from .payment import pay_with_paystack, pay_with_stripe
import os

app = FastAPI()

# Simple in-memory user store
users = {}
FREE_CREDITS = 10
COST_PER_ACTION = 1

class SignUp(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class Action(BaseModel):
    email: str
    action: str

class AddFunds(BaseModel):
    email: str
    amount: int
    provider: str = "mock"

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env if present
load_dotenv(Path(__file__).resolve().parents[2] / '.env')

API_BASE = os.getenv('API_BASE', 'https://api.example.com')
SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')

app = FastAPI()

class Idea(BaseModel):
    idea: str

class Message(BaseModel):
    input: str

@app.get('/')
def read_root():
    return {'message': 'RaiziomFix API'}

@app.post('/signup')
def signup(data: SignUp):
    if data.email in users:
        raise HTTPException(status_code=400, detail='User exists')
    user = User(email=data.email, password=data.password, credits=FREE_CREDITS)
    user.logs.append(Transaction(amount=FREE_CREDITS, description='Free trial credits'))
    users[data.email] = user
    return {'message': 'signed up', 'credits': user.credits}

@app.post('/login')
def login(data: Login):
    user = users.get(data.email)
    if not user or user.password != data.password:
        raise HTTPException(status_code=400, detail='Invalid credentials')
    return {'message': 'logged in'}

@app.get('/wallet/{email}')
def wallet(email: str):
    user = users.get(email)
    if not user:
        raise HTTPException(status_code=404, detail='Not found')
    return {'credits': user.credits}

@app.get('/earnings/{email}')
def earnings(email: str):
    user = users.get(email)
    if not user:
        raise HTTPException(status_code=404, detail='Not found')
    return {'logs': [t.__dict__ for t in user.logs]}

@app.post('/action')
def do_action(data: Action):
    user = users.get(data.email)
    if not user:
        raise HTTPException(status_code=404, detail='Not found')
    if user.credits < COST_PER_ACTION:
        raise HTTPException(status_code=400, detail='Insufficient credits')
    user.credits -= COST_PER_ACTION
    user.logs.append(Transaction(amount=-COST_PER_ACTION, description=data.action))
    return {'credits': user.credits}

@app.post('/add_funds')
def add_funds(data: AddFunds):
    user = users.get(data.email)
    if not user:
        raise HTTPException(status_code=404, detail='Not found')
    # Payment integration stub
    if data.provider.lower() == 'paystack':
        pay_with_paystack(data.amount, data.email)
    elif data.provider.lower() == 'stripe':
        pay_with_stripe(data.amount, data.email)
    # For now we just credit the wallet
    user.credits += data.amount
    user.logs.append(Transaction(amount=data.amount, description=f'Added via {data.provider}'))
    return {'credits': user.credits}
@app.post('/idea')
def receive_idea(idea: Idea):
    # Placeholder for storing idea or forwarding to a service
    return {'received': idea.idea}

@app.post('/ai/respond')
def ai_respond(message: Message):
    reply = f"Echo from {API_BASE}: {message.input}"
    return {'reply': reply}

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import stripe

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext
from uuid import uuid4
from typing import Dict, List
import os
import json

app = FastAPI()

# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory stores
users: Dict[str, str] = {}
tokens: Dict[str, str] = {}

class UserCredentials(BaseModel):
    email: str
    password: str

class Idea(BaseModel):
    idea: str

class AIInput(BaseModel):
    input: str

@app.get("/")
def read_root():
    return {"message": "RaiziomFix API"}


@app.post("/create-checkout-session")
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": os.getenv("STRIPE_PRICE_ID"),
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=f"{os.getenv('FRONTEND_URL', 'http://localhost:3000')}/?success=true",
            cancel_url=f"{os.getenv('FRONTEND_URL', 'http://localhost:3000')}/?canceled=true",
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.post("/register")
def register(creds: UserCredentials):
    if creds.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[creds.email] = pwd_context.hash(creds.password)
    return {"status": "registered"}

@app.post("/login")
def login(creds: UserCredentials):
    stored = users.get(creds.email)
    if not stored or not pwd_context.verify(creds.password, stored):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = str(uuid4())
    tokens[token] = creds.email
    return {"token": token}

# Dependency to check token
def get_current_user(token: str | None = None):
    if not token or token not in tokens:
        raise HTTPException(status_code=401, detail="Invalid token")
    return tokens[token]

@app.get("/plugins")
def list_plugins(user: str = Depends(get_current_user)):
    plugins_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "plugins")
    results: List[Dict] = []
    if os.path.isdir(plugins_path):
        for name in os.listdir(plugins_path):
            f = os.path.join(plugins_path, name, "plugin.json")
            if os.path.isfile(f):
                with open(f) as fp:
                    try:
                        results.append(json.load(fp))
                    except json.JSONDecodeError:
                        continue
    return results

@app.post("/idea")
def send_idea(idea: Idea, user: str = Depends(get_current_user)):
    # Simple echo for now
    return {"received": idea.idea}

@app.post("/ai/respond")
def ai_respond(inp: AIInput, user: str = Depends(get_current_user)):
    text = inp.input
    # Naive AI: reverse the text
    reply = text[::-1]
    return {"reply": reply}

