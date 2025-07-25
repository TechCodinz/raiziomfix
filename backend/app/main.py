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
