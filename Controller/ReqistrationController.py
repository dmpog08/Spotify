from Class.Application import Application as app
from Models.User import User
from flask import redirect, render_template
from Class.Interfase.IController import IController


class ReqistrationController(IController):
    def __init__(self, view=None, model=None, login_user=None):
        self.__view = view
        self.__model = model
        self.__login_user = login_user

    def __call__(self, *args, **kwargs):
        if self.__model.validate_on_submit():
            if self.__model.password.data != self.__model.password_again.data:
                return render_template('register.html', title='Регистрация',
                                       form=self.__model, message="Пароли не совпадают")
            if app().context.query(User).filter(User.email == self.__model.email.data).first():
                return render_template('register.html', title='Регистрация',
                                       form=self.__model, message="Такой пользователь уже есть")
            user = User(name=self.__model.name.data,
                        email=self.__model.email.data,
                        sename=self.__model.sename.data,
                        nickname=self.__model.nickname.data,
                        phone=self.__model.phone.data)
            user.password = self.__model.password.data
            app().context.add(user)
            app().context.commit()
            self.__login_user(user, remember=True)
            return redirect("/")
        return render_template('register.html', title='Регистрация', form=self.__model)