#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :request.py
@说明        :上下文管理
@时间        :2021/01/21 16:45:24
@作者        :张强
@版本        :1.0
'''

'''
Flask 有两种上下文：程序上下文和请求上下文
    变量名            上下文                 说明
current_app        程序上下文        当前激活程序的程序实例
    g              程序上下文        处理请求时用作临时存储的对象。每次请求都会重置这个变量
    request        请求上下文        请求对相关，封装了客户端发出的HTTP请求中的内容
    session        请求上下文        用户会话，用于存在请求之间需要“记住”的值的词典
'''

from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>你的浏览器是 %s</p>' % user_agent

if __name__ == "__main__":
    app.run()



''' 上下文应用
>>>from hello import app
>>>from flask import current_app
>>>current_app.name
>>>app_ctx =app.app_context()
>>>app_ctx.push()
>>>current_app.name
>>>app_ctx.pop()
'''