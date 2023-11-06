from Class.Application import Application as app
from Models.Comment import Comment
from Models.User import User
from flask import jsonify, make_response
from Class.Interfase.IController import IController
from flask_login import current_user
from Class.MakeResponse import MakeResponse


class LoadCommentsController(IController):
    def __call__(self, massed, *args, **kwargs):
        req = massed.get_json()
        comments = app().context.query(Comment).filter(Comment.id_sound == req["id"]).all()
        comments_response = {
            "data": []
        }
        for i in range(len(comments)):
            comments[i] = MakeResponse.make_response_comments(comments[i].__dict__)
        for i in comments:
            user = app().context.query(User).filter(User.id == i["id_user"]).first()
            comments_response["data"].append({
                "user": {
                    "nickname": user.nickname,
                    "icon": user.icon
                },
                "comment": {
                    "text": i["text"],
                    "date": i["created_date"]
                }
            })
        res = make_response(jsonify(comments_response), 200)
        print(comments_response)
        return res