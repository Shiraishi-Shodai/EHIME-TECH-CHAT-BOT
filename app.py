# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 必要なものをインポート

from flask import Flask, render_template

app = Flask(__name__, template_folder='template')   #Flaskのインスタンス化(デフォルトでmainになる)

@app.route('/') #ルートからのパスを設定
def index():
    return render_template('main.html')

# Flaskで必要なもの、port=8000番
if __name__ == '__main__':
    app.run(port=8000,debug=True) #Flaskを実行