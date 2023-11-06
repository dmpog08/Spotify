import os
from werkzeug.utils import secure_filename
from Class.Application import Application as app
from Models.User import User
from flask import redirect, render_template
from Class.Interfase.IController import IController
from flask_login import current_user


class MyProfileController(IController):
    def __init__(self, view=None, model=None):
        self.__view = view
        self.__model = model

    def __call__(self, *args, **kwargs):
        if self.__model.validate_on_submit():
            img = self.__model.img.data
            if img is not None:
                filename_img = secure_filename(img.filename).split(".")
                filename_img = os.path.join('img', os.urandom(15).hex() + "." + filename_img[-1])
                img.save(os.path.join(app().app.config["FILE_DIR"], "static", filename_img))
                filename_img = filename_img.replace('\\', "/")
            else:
                filename_img = current_user.icon

            now_user = app().context.query(User).filter(User.id == current_user.id).first()
            now_user.name = self.__model.name.data
            now_user.email = self.__model.email.data
            now_user.sename = self.__model.sename.data
            now_user.nickname = self.__model.nickname.data
            now_user.phone = self.__model.phone.data
            now_user.birthday = self.__model.birthday.data
            now_user.icon = filename_img

            app().context.commit()
            return render_template('profile.html', title='Профиль', form=self.__model)
        return render_template('profile.html', title='Профиль', form=self.__model)
