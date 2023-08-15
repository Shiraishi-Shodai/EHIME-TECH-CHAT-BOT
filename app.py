from flask import Flask, render_template

app = Flask(__name__)   #Flaskのインスタンス化(デフォルトでmainになる)

@app.route('/') #ルートからのパスを設定
def index():
    html = render_template('index.html', a= '変数なう')
    return html

@app.route('/good') #ルートからのパスを設定
def good():
    return 'good'
if __name__ == '__main__':
    app.run(debug=True) #Flaskを実行