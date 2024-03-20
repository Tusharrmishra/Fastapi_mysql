from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    name: str
    email: str
    password: str


class User(UserBase):
    
    class Config:
        orm_mode = True
