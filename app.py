# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 必要なものをインポート

from flask import Flask, render_template, request, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from deep_translator import GoogleTranslator


app = Flask(__name__, template_folder='template')   #Flaskのインスタンス化(デフォルトでmainになる)


# チャットボット指定
bot = ChatBot('MyBot')
# 訓練用のリスト
conversation = [
    "Hello", # こんにちは
    "Hi there!", # こんにちは！
    "How are you?", # お元気ですか？
    "I am good.", # 私は元気です。
    "That is good to hear.", # それは良かった。
    "Thank you", # ありがとうございました
    "You are welcome.", # どう致しまして。
]

trainer = ListTrainer(bot)
trainer.train(conversation)

array = []
# 回答データ
answer_data = {
    1:"➀の解答です",
    2:"➁の解答です",
    3:"➂の解答です",
    4:"➃の解答です",
}

def find_answer(question, answer_data):
    # 数字でないなら数字を入力してくださいと返す
    # ・isdecimal は文字列中のすべての文字が 10進数で使われる文字で、かつ 1文字以上ある場合に真を返す関数
    if not question.isdecimal():
        return "数字を入力してください"
    # 入力した数字がanswer_dataのキーにないとき
    if int(question) not in answer_data:
        return "回答が登録されていません"
    
    return answer_data[int(question)]

@app.route('/', methods=['GET', 'POST']) #ルートからのパスを設定
def index():
    if request.method == 'GET':

        return render_template('main.html')
    
    # POSTで受け取った値を取得
    question = request.form['question']
    if question.endswith('translate'):
        # 末尾のtranslateを削除
        question = question.rstrip('translate')
        # questionを日本語に翻訳
        answer = GoogleTranslator(source='auto',target='ja').translate(question)
    else:
        # # quesitonをキーとし、対応する回答を取得
        # answer = find_answer(question, answer_data)
        answer = bot.get_response(question)
    # array配列に辞書を追加
    array.append({
        question: answer
    })
    # question,answerをmain.htmlに渡し、main.htmlを表示する
    return render_template('main.html', array=array)

# Flaskで必要なもの、port=8000番
# このファイルを直接実行しているかを判断
if __name__ == '__main__':
    app.run(port=8000,debug=True) #Flaskを実行