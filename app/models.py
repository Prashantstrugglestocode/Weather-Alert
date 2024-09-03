from sqlalchemy import Column, Integer, String, TIMESTAMP,text
from .database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    
    id = Column(Integer, primary_key=True,nullable = False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, nullable=False)
    report_time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
