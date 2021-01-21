#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :2-1Hello.py
@说明        :
@时间        :2021/01/21 16:34:17
@作者        :张强
@版本        :1.0
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

if __name__ == "__main__":
    app.run()