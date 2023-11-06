import pickle
from flask import url_for


class MakeResponse:
    @classmethod
    def make_response_sound(cls, mas):
        del mas['_sa_instance_state']
        for i in mas:
            if type(mas[i]) == bytes:
                mas[i] = len(pickle.loads(mas[i]))
        mas["created_date"] = mas["created_date"].strftime("%d/%m/%Y")
        mas["img"] = url_for("static", filename=mas["img"].replace('\\', "/"))
        mas["file_name"] = url_for("static", filename=mas["file_name"].replace('\\', "/"))
        return mas

    @classmethod
    def make_response_list_music(cls, mas):
        del mas['_sa_instance_state']
        for i in mas:
            if type(mas[i]) == bytes:
                mas[i] = pickle.loads(mas[i])
        return mas

    @classmethod
    def make_response_comments(cls, mas):
        del mas['_sa_instance_state']
        return mas