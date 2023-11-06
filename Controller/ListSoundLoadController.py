from Class.Application import Application as app
from Models.ListSound import ListSound
from flask import jsonify, make_response
from Class.Interfase.IController import IController
from flask_login import current_user
from Class.MakeResponse import MakeResponse
from Controller.GetMusicController import GetMusicController


class ListSoundLoadController(IController):
    def __call__(self, massed, *args, **kwargs):
        get_music = GetMusicController()
        req = massed.get_json()
        user = app().context.query(ListSound).filter(ListSound.id_user == current_user.id).first()
        if user is None:
            list_sound = ListSound(id_user=current_user.id,
                                   name="Мой плейлист")
            app().context.add(list_sound)
            app().context.commit()
        list_sound = app().context.query(ListSound).filter(ListSound.id_user == current_user.id).all()
        for i in range(len(list_sound)):
            list_sound[i] = MakeResponse.make_response_list_music(list_sound[i].__dict__)

        for play_list in list_sound:
            sound = []
            for id_sound in play_list["sounds"]:
                 sound.append(get_music({"id": id_sound}))
            play_list["sounds"] = sound
        res = make_response(jsonify({"data": list_sound}), 200)
        return res