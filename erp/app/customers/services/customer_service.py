from typing import List
from sqlalchemy.orm import Session
from app.models.customer_model import Customer, Transaction
from app.schemas.customer_schemas import CustomerCreate, TransactionCreate

def get_customer(db: Session, customer_id: int) -> Customer:
    return db.query(Customer).filter(Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100) -> List[Customer]:
    return db.query(Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: CustomerCreate) -> Customer:
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_transaction(db: Session, transaction: TransactionCreate, customer_id: int) -> Transaction:
    db_transaction = Transaction(**transaction.dict(), customer_id=customer_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session, customer_id: int) -> List[Transaction]:
    return db.query(Transaction).filter(Transaction.customer_id == customer_id).all()
