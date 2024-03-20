from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_person = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    address = Column(String)
    payment_terms = Column(String)
    credit_limit = Column(Float)

    transactions = relationship("Transaction", back_populates="customer")

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    transaction_date = Column(DateTime)
    amount = Column(Float)

    customer = relationship("Customer", back_populates="transactions")
