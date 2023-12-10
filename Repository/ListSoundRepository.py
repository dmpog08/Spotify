from sqlalchemy.orm import Session
from Models.ListSound import ListSound, ListSoundToSound, Share
from Models.Sound import Sound
from uuid import uuid4


class ListSoundRepository:
    def __init__(self, session: Session):
        self.__session: Session = session

    def add_to_list_sound(self, id_list_sound: int, id_sound: int):

        sound = self.__session.get(Sound, id_sound)
        list_sound = self.__session.get(ListSound, id_list_sound)

        try:
            self.__session.add(ListSoundToSound(
                id_list_sound=list_sound.id,
                id_sound=sound.id
            ))
            self.__session.commit()
        except:
            self.__session.rollback()
            raise ConnectionError("ошибка добавления в плейлист")

    def get_sound_to_list_sound(self, id_sound: int, id_list_sound: int) -> Sound:
        return self.__session.query(ListSoundToSound).\
            where(ListSoundToSound.id_sound == id_sound).\
            where(ListSoundToSound.id_list_sound == id_list_sound).first()

    def get(self, id_list_sound: int) -> ListSound:
        return self.__session.get(ListSound, id_list_sound)

    def add_list_sound(self, id_user: int, name: str):
        try:
            self.__session.add(ListSound(
                id_user=id_user,
                name=name
            ))
            self.__session.commit()
        except:
            self.__session.rollback()

    def get_list_sound_by_user_id(self, id_user: int) -> list[ListSound]:
        return self.__session.query(ListSound).where(ListSound.id_user == id_user).all()


    def get_share(self, id_list_sound: int) -> Share:
        return self.__session.query(Share).where(Share.id_list_sound == id_list_sound).first()

    def create_share(self, id_list_sound: int) -> Share:
        entity = Share(
            id_trace=str(uuid4()).replace("-", ""),
            id_list_sound=id_list_sound,
        )
        try:
            self.__session.add(entity)
            self.__session.commit()
            return entity
        except:
            self.__session.rollback()
            return None

    def get_share_by_ref(self, id_trace: str) -> Share:
        return self.__session.query(Share).where(Share.id_trace == id_trace).first()
