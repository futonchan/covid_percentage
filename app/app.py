# アプリの動き(変数？)を書くところらしい

#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request

from models.models import OnegaiContent
from models.database import db_session # 普通の変数もインポートできるんだ
from datetime import datetime

app = Flask(__name__) #Flaskインスタンスをappで宣言


# @...デコレータ、真下の行の関数を引数にとる
# 呼び出し自体は真下の行の関数でおｋ、実行自体はデコレータが実行される
@app.route("/") #「/」へアクセスがあった場合
@app.route("/index") #「/index」へアクセスがあった場合
def index():

    name = request.args.get("name")
    all_onegai = OnegaiContent.query.all()

    return render_template("index.html",name=name,all_onegai=all_onegai) # index.htmlで使えるようになる

@app.route("/index", methods=["post"]) # index.htmlからPOSTを受け取る側
def post():
    name = request.form["name"] # index.htmlのフォームのname指定した変数をnameに代入
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html",name=name,all_onegai=all_onegai) # index.htmlで使えるようになる

@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    return index() # returnに関数渡すこともできる

if __name__ == "__main__":
    app.run(debug=True)
