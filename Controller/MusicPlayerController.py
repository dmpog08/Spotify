from Class.Application import Application as app
from Class.Interfase.IController import IController
from Models.Sound import Sound
import mimetypes
import os
import re

from flask import request, send_file, Response
from zlib import adler32


class MusicPlayerController(IController):
    def __init__(self, view=None, model=None, login_user=None):
        self.__view = view
        self.__model = model
        self.__login_user = login_user

    def send_file_partial(self, path):
        range_header = request.headers.get('Range', None)
        if not range_header:
            return send_file(path)

        size = os.path.getsize(path)
        byte1, byte2 = 0, None

        m = re.search('(\d+)-(\d*)', range_header)
        g = m.groups()

        if g[0]:
            byte1 = int(g[0])
        if g[1]:
            byte2 = int(g[1])

        length = size - byte1
        if byte2 is not None:
            length = byte2 - byte1

        data = None
        with open(path, 'rb') as f:
            f.seek(byte1)
            data = f.read(length)

        rv = Response(data,
                      206,
                      mimetype=mimetypes.guess_type(path)[0],
                      direct_passthrough=True)
        rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))
        rv.set_etag('flask-%s-%s-%s' % (
            os.path.getmtime(path),
            os.path.getsize(path),
            adler32(
                path.encode('utf-8') if isinstance(path, str)
                else path
            ) & 0xffffffff
        ))
        rv.headers.add('Cache-Control', 'no-cache')
        return rv

    def __call__(self, song_id: int):
        sound = app().context.query(Sound).filter(Sound.id == song_id).first()
        return self.send_file_partial(f"static/{sound.file_name}")