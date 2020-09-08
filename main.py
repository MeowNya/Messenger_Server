# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'MeowNya'


from flask import Flask
from datetime import datetime

app = Flask(__name__)
NAME = 'Messenger Server'


@app.route('/')
def index():
    return """<center><font size="20" face="Times New Roman"><b>You're Welcome!</b>
     <br> <a href='/status'>Статус</a></font></center>"""


@app.route("/status")
def status():
    return {
        'status': 'OK',
        'name': NAME,
        'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    }


if __name__ == '__main__':
    app.run()