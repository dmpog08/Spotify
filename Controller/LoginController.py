from Class.Application import Application as app
from Models.User import User
from flask import redirect, render_template
from Class.Interfase.IController import IController


class LoginController(IController):
    def __init__(self, view=None, model=None, login_user=None):
        self.__view = view
        self.__model = model
        self.__login_user = login_user

    def __call__(self, *args, **kwargs):
        if self.__model.validate_on_submit():
            user = app().context.query(User).filter(User.email == self.__model.email.data).first()
            if user and user.check_password(self.__model.password.data):
                self.__login_user(user, remember=self.__model.remember_me.data)
                return redirect("/")
            return render_template('login.html', message="Неправильный логин или пароль", form=self.__model)
        return render_template('login.html', title='Авторизация', form=self.__model)