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

from Class.MakeResponse import MakeResponse

from Controller.MusicPlayerController import MusicPlayerController

from forms.LoginForm import LoginForm
from forms.ReqistrationForm import RegisterForm
from forms.UploadMusicForm import UploadMusicForm
from forms.ProfileForm import ProfileForm

from Service import PlayListService

from Models.User import User

import os

from flask import Flask, render_template, redirect, request, abort, session, make_response, jsonify, Response, url_for
from flask_login import login_user, logout_user, login_required, current_user


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


'''@app.route("/list_sound_view",  methods=['GET', 'POST'])
def list_sound_view():
    controller = ListSoundLoadController()
    return controller(request)'''


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


@app.route('/user/play_list/add/<int:id_play_list>/<int:id_sound>')
@login_required
def add_play_list(id_play_list: int, id_sound: int):
    service = PlayListService(Application().context)
    message = service.add_to_list_sound(id_play_list, id_sound)
    print(message)
    return redirect(url_for("index"))


@app.route('/user/play_list/get/<int:id_sound>')
@login_required
def get_play_list_by_user(id_sound: int):
    service = PlayListService(Application().context)
    list_sound = service.get_play_list(current_user.id)
    return render_template("add_to_list_sound.html", play_lists=list_sound, id_sound=id_sound)


@app.route('/user/play_list/get/')
@login_required
def get_play_list():
    service = PlayListService(Application().context)
    list_sound = service.get_play_list(current_user.id)
    return render_template("list_sound.html", play_lists=list_sound)


@app.route('/user/play_list/<int:id_play_list>/sounds/')
@login_required
def sounds_play_list(id_play_list: int):
    service = PlayListService(Application().context)
    sounds = service.get_play_list_by_id(id_play_list)
    share_entity = service.get_share(id_play_list)
    ref = ""
    if share_entity is None:
        ref = None
    else:
        ref = url_for('share_play_list', ref=share_entity.id_trace)
    return render_template("play_list_sounds.html", sounds=sounds.sounds, ref_share=ref, id_play_list=id_play_list)


@app.route('/user/play_list/<int:id_play_list>/share')
@login_required
def share(id_play_list: int):
    service = PlayListService(Application().context)
    service.share(id_play_list)
    return redirect(url_for("sounds_play_list", id_play_list=id_play_list))


@app.route("/share/play_list")
def share_play_list():
    trace_id = request.args.get("ref")

    service = PlayListService(Application().context)

    sounds = service.get_play_list_share(trace_id)
    return render_template("play_list_sounds.html", sounds=sounds.sounds, ref_share="anon")


def main():
    Application().create_context("db/sound.db")
    app.run(debug=True)


if __name__ == '__main__':
    main()
