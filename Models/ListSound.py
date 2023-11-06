import datetime
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from Class.Application import Application
import pickle


class ListSound(Application().model):
    __tablename__ = "ListsSound"

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    name = Column(String, nullable=True)
    sounds = Column(LargeBinary, nullable=True, default=pickle.dumps(set()))