import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Class.Application import Application
from Models.Sound import Sound
import pickle
from uuid import uuid4


class ListSound(Application().model):
    __tablename__ = "list_sound"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer)
    name = Column(String, nullable=True)
    icon = Column(String, nullable=False, default="img/lol.png")
    sounds = relationship(
        "Sound", secondary="list_sound_to_sound"
    )


class ListSoundToSound(Application().model):
    __tablename__ = "list_sound_to_sound"
    id_list_sound = Column(ForeignKey("list_sound.id"), primary_key=True)
    id_sound = Column(ForeignKey("sounds.id"), primary_key=True)


class Share(Application().model):
    __tablename__ = "share"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_trace = Column(String, nullable=False)
    id_list_sound = Column(ForeignKey("list_sound.id"))
    list_sound = relationship("ListSound")