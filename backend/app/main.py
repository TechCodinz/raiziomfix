# 🌱 Raiziomfix Core Engine – To be evolved into Raiziom

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext
from uuid import uuid4
from typing import Dict, List
from pathlib import Path
import os
import json
from dotenv import load_dotenv

from .models import User, Transaction
from .payment import pay_with_paystack, pay_with_stripe

# Load environment variables
load_dotenv(Path(__file__).resolve().parents[2] / '.env')

app = FastAPI()
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
wallets: Dict[str, User] = {}

FREE_CREDITS = 10
COST_PER_ACTION = 1

class UserCredentials(BaseModel):
    email: str
    password: str

class Action(BaseModel):
    email: str
    action: str

class AddFunds(BaseModel):
    email: str
    amount: int
    provider: str = "mock"

class Idea(BaseModel):
    idea: str

class AIInput(BaseModel):
    input: str

@app.get("/")
def read_root():
    return {"message": "RaiziomFix API"}

# 🧠 Core logic: part of Raiziom engine
@app.post("/register")
def register(creds: UserCredentials):
    if creds.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[creds.email] = pwd_context.hash(creds.password)
    wallets[creds.email] = User(email=creds.email, password=creds.password, credits=FREE_CREDITS)
    wallets[creds.email].logs.append(Transaction(amount=FREE_CREDITS, description="Free trial credits"))
    return {"status": "registered"}

@app.post("/signup")
def signup(creds: UserCredentials):
    return register(creds)

# 🧠 Core logic: part of Raiziom engine
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

@app.get("/wallet/{email}")
def wallet(email: str):
    user = wallets.get(email)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return {"credits": user.credits}

@app.get("/earnings/{email}")
def earnings(email: str):
    user = wallets.get(email)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return {"logs": [t.__dict__ for t in user.logs]}

@app.post("/action")
def do_action(data: Action):
    user = wallets.get(data.email)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    if user.credits < COST_PER_ACTION:
        raise HTTPException(status_code=400, detail="Insufficient credits")
    user.credits -= COST_PER_ACTION
    user.logs.append(Transaction(amount=-COST_PER_ACTION, description=data.action))
    return {"credits": user.credits}

@app.post("/add_funds")
def add_funds(data: AddFunds):
    user = wallets.get(data.email)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    if data.provider.lower() == "paystack":
        pay_with_paystack(data.amount, data.email)
    elif data.provider.lower() == "stripe":
        pay_with_stripe(data.amount, data.email)
    user.credits += data.amount
    user.logs.append(Transaction(amount=data.amount, description=f"Added via {data.provider}"))
    return {"credits": user.credits}

# 🧠 Core logic: part of Raiziom engine
@app.post("/create-checkout-session")
def create_checkout_session():
    try:
        import stripe
        stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{"price": os.getenv("STRIPE_PRICE_ID"), "quantity": 1}],
            mode="payment",
            success_url=f"{os.getenv('FRONTEND_URL', 'http://localhost:3000')}/?success=true",
            cancel_url=f"{os.getenv('FRONTEND_URL', 'http://localhost:3000')}/?canceled=true",
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/plugins")
def list_plugins(token: str = Depends(get_current_user)):
    plugins_path = os.path.join(Path(__file__).resolve().parents[1], "plugins")
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
def send_idea(idea: Idea, token: str = Depends(get_current_user)):
    return {"received": idea.idea}

@app.post("/ai/respond")
def ai_respond(inp: AIInput, token: str = Depends(get_current_user)):
    text = inp.input
    reply = text[::-1]
    return {"reply": reply}
