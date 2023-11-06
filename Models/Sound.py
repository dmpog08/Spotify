import datetime
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from Class.Application import Application
import pickle


class Sound(Application().model):
    __tablename__ = "sounds"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    img = Column(String, nullable=True)
    file_name = Column(String, nullable=True)
    teg = Column(String, nullable=True)
    listening = Column(LargeBinary, nullable=True, default=pickle.dumps([]))
    like = Column(LargeBinary, nullable=True, default=pickle.dumps([]))
    dislike = Column(LargeBinary, nullable=True, default=pickle.dumps([]))
    created_date = Column(DateTime, default=datetime.datetime.now)
    id_user = Column(Integer)

