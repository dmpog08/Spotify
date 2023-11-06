from Class.Application import Application as app
from Models.Sound import Sound
from werkzeug.utils import secure_filename
from flask import redirect, render_template
from Class.Interfase.IController import IController
from flask_login import current_user
import os


class UploadMusicController(IController):
    def __init__(self, view=None, model=None):
        self.__view = view
        self.__model = model

    def __call__(self, *args, **kwargs):
        if self.__model.validate_on_submit():
            img = self.__model.img.data
            music = self.__model.music.data
            filename_img = secure_filename(img.filename).split(".")
            filename_music = secure_filename(music.filename).split(".")

            filename_img = os.path.join('img', "sound", os.urandom(15).hex() + "." + filename_img[-1])
            filename_music = os.path.join('sound', os.urandom(15).hex() + "." + filename_music[-1])

            sound = Sound(name=self.__model.name.data,
                          img=filename_img.replace('\\', "/"),
                          file_name=filename_music.replace('\\', "/"),
                          teg=self.__model.tag.data,
                          id_user=current_user.id)

            app().context.add(sound)
            app().context.commit()
            img.save(os.path.join(app().app.config["FILE_DIR"], "static", filename_img))
            music.save(os.path.join(app().app.config["FILE_DIR"], "static", filename_music))
            #return redirect("/")
        return render_template('load_music.html', title='Регистрация', form=self.__model)