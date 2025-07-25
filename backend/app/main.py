
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

