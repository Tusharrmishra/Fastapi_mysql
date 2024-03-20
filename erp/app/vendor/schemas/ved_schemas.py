from pydantic import BaseModel

class VendorBase(BaseModel):
    name: str
    contact_person: str
    email: str
    phone_number: str
    address: str
    payment: str

class VendorCreate(VendorBase):
    pass

class Vendor(VendorBase):
    id: int

    class Config:
        orm_mode = True
