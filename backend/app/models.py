from dataclasses import dataclass, field
from typing import List
import datetime

@dataclass
class Transaction:
    amount: int
    description: str
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.utcnow)

@dataclass
class User:
    email: str
    password: str
    credits: int = 0
    logs: List[Transaction] = field(default_factory=list)
