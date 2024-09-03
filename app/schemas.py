from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    city: str
    report_time: str

    class Config:
        orm_mode = True