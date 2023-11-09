from Class.Application import Application

from Controller.ListSoundLoadController import ListSoundLoadController
from Controller.LoadCommentsController import LoadCommentsController
from Controller.LoadMusicController import LoadMusicController
from Controller.LoginController import LoginController
from Controller.ReqistrationController import ReqistrationController
from Controller.UploadCommentController import UploadCommentController
from Controller.UploadMusicController import UploadMusicController
from Controller.ProfileController import MyProfileController
from Controller.GetMusicController import GetMusicController

from Controller.MusicPlayerController import MusicPlayerController

from forms.LoginForm import LoginForm
from forms.ReqistrationForm import RegisterForm
from forms.UploadMusicForm import UploadMusicForm
from forms.ProfileForm import ProfileForm

from Models.User import User

import os

from flask import Flask, render_template, redirect, request, abort, session, make_response, jsonify, Response
from flask_login import login_user, logout_user, login_required
from sqlalchemy import desc
from forms.comment import Comment
from forms.fake_quest import Fake_Quest

Application().app = Flask(__name__)
app = Application().app

app.config["FILE_DIR"] = os.path.dirname(os.path.abspath(__file__))

login_manager = Application().login_manager


@login_manager.user_loader
def load_user(user_id):
    db_sess = Application().context
    return db_sess.query(User).get(user_id)

@app.route("/", methods=['GET', 'POST'])
def index():
    state = 'Медиатека'
    return render_template("index.html", title=state, quest_list=[], state=state, form=ProfileForm())


@app.route("/upload_music",  methods=['GET', 'POST'])
@login_required
def upload_music():
    controller = UploadMusicController(model=UploadMusicForm())
    return controller()


@app.route("/load_view_comments",  methods=['GET', 'POST'])
def load_view_comments():
    controller = LoadCommentsController()
    return controller(request)


@app.route("/load_music_view",  methods=['GET', 'POST'])
def load_music_view():
    controller = LoadMusicController()
    return controller(request)


@app.route("/upload_comment",  methods=['GET', 'POST'])
@login_required
def upload_comment():
    controller = UploadCommentController()
    return controller(request)


@app.route("/list_sound_view",  methods=['GET', 'POST'])
def list_sound_view():
    controller = ListSoundLoadController()
    return controller(request)


@app.route("/get_music",  methods=['GET', 'POST'])
def get_music():
    controller = GetMusicController()
    return make_response(jsonify({"data": controller(request.get_json())}), 200)


'''@app.route("/add_list_music",  methods=['GET', 'POST'])
@login_required
def add_list_music():
    controller = AddListMusicController()
    return controller(request)'''


@app.route("/my_profile",  methods=['GET', 'POST'])
@login_required
def my_profile():
    model = ProfileForm()
    controller = MyProfileController(model=model)
    return controller()


@app.route('/login', methods=['GET', 'POST'])
def login():
    controller = LoginController(model=LoginForm(), login_user=login_user)
    return controller()


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    controller = ReqistrationController(model=RegisterForm(), login_user=login_user)
    return controller()

@app.route('/play/<int:stream_id>')
def streammp3(stream_id):
    controller = MusicPlayerController(model=None, login_user=None)
    return controller(stream_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    Application().create_context("db/sound.db")
    app.run(debug=True)


if __name__ == '__main__':
    main()
