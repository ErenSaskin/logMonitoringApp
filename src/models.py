from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Log(Base):
    
    __tablename__ = "log"
    id = Column(Integer, primary_key = True, index = True)
    methodType = Column(String)
    ms = Column(Integer)
    timestamp = Column(Integer)
    