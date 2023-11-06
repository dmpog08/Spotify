import datetime
from sqlalchemy import Column, Integer, String, DateTime
from Class.Application import Application


class Comment(Application().model):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.datetime.now)
    id_user = Column(Integer)
    id_sound = Column(Integer)
