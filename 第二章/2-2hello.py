#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :2-2hello.py
@说明        :
@时间        :2021/01/21 16:35:51
@作者        :张强
@版本        :1.0
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name
    
if __name__ == "__main__":
    app.run()