from sqlalchemy.orm import Session
from Repository import ListSoundRepository
from Models.ListSound import ListSound, Share


class PlayListService:
    def __init__(self, session: Session):
        self.__list_sound_repository: ListSoundRepository = ListSoundRepository(session)

    def add_to_list_sound(self, id_list_sound: int, id_sound: int):
        try:
            sound = self.__list_sound_repository.get_sound_to_list_sound(id_sound, id_list_sound)
            if sound is None:
                self.__list_sound_repository.add_to_list_sound(id_list_sound, id_sound)
                return {"message": "Добавлен в плелист"}
            else:
                return {"message": "Музыка уже существует в плейлите"}
        except ConnectionError:
            return {"message": "Ошибка добавления"}

    def get_play_list(self, id_user: int) -> list[ListSound]:
        return self.__list_sound_repository.get_list_sound_by_user_id(id_user)

    def get_play_list_by_id(self, id_play_list: int) -> ListSound:
        return self.__list_sound_repository.get(id_play_list)

    def get_share(self, id_play_list: int) -> Share:
        ref_share = self.__list_sound_repository.get_share(id_play_list)
        return ref_share

    def share(self, id_play_list: int):
        ref_share = self.get_share(id_play_list)
        if ref_share is None:
            ref_share = self.__list_sound_repository.create_share(id_play_list)

    def get_play_list_share(self, id_trace: str) -> ListSound:
        share = self.__list_sound_repository.get_share_by_ref(id_trace)
        return self.get_play_list_by_id(share.id_list_sound)

