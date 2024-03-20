from pydantic import BaseModel
from typing import List
from datetime import datetime, date, time, timezone

class CustomerBase(BaseModel):
    name: str
    contact_person: str
    email: str
    phone_number: str
    address: str
    payment_terms: str
    credit_limit: float

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    customer_id: int
    transaction_date: datetime
    amount: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    customer: Customer

    class Config:
        orm_mode = True

class CustomerWithTransactions(Customer):
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True
