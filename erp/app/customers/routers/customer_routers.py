from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import SessionLocal
from erp.app.customers.services.customer_service import (
    get_customer,
    get_customers,
    create_customer,
    create_transaction,
    get_transactions,
)
from app.schemas.customer_schemas import Customer, CustomerCreate, Transaction, TransactionCreate

router = APIRouter()

@router.get("/customers/{customer_id}", response_model=Customer)
def get_customer_endpoint(customer_id: int, db: Session = Depends(SessionLocal)):
    return get_customer(db, customer_id)

@router.get("/customers", response_model=List[Customer])
def get_customers_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(SessionLocal)):
    return get_customers(db, skip, limit)

@router.post("/customers", response_model=Customer)
def create_customer_endpoint(customer: CustomerCreate, db: Session = Depends(SessionLocal)):
    return create_customer(db, customer)

@router.put("/customers/{customer_id}", response_model=Customer)
def update_customer_endpoint(customer_id: int, customer: CustomerCreate, db: Session = Depends(SessionLocal)):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        for key, value in customer.dict().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

@router.delete("/customers/{customer_id}")
def delete_customer_endpoint(customer_id: int, db: Session = Depends(SessionLocal)):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
        return {"message": "Customer deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

@router.post("/transactions/{customer_id}", response_model=Transaction)
def create_transaction_endpoint(customer_id: int, transaction: TransactionCreate, db: Session = Depends(SessionLocal)):
    return create_transaction(db, transaction, customer_id)

@router.get("/transactions/{customer_id}", response_model=List[Transaction])
def get_transactions_endpoint(customer_id: int, db: Session = Depends(SessionLocal)):
    return get_transactions(db, customer_id)

@router.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction_endpoint(transaction_id: int, transaction: TransactionCreate, db: Session = Depends(SessionLocal)):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction:
        for key, value in transaction.dict().items():
            setattr(db_transaction, key, value)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")

@router.delete("/transactions/{transaction_id}")
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(SessionLocal)):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return {"message": "Transaction deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")
