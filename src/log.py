from typing import List, Optional
from . import database
from sqlalchemy.orm import Session
from fastapi import Depends
from . import models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

class Log:
    def __init__(self, methodType, ms, timestamp):
        self.methodType = methodType
        self.ms = ms
        self.timestamp = timestamp


    def saveToDatabase(self, db: Session = database.get_db()):
        new_log = models.Log(
            methodType = self.methodType,
            ms = self.ms,
            timestamp = self.timestamp
        )
        db.add(new_log)
        db.commit()
        db.refresh(new_log)
        print("Log created ..")