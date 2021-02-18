# アプリの動き(変数？)を書くところらしい

#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap

from models.models import OnegaiContent
from models.database import db_session # 普通の変数もインポートできるんだ
from datetime import datetime

app = Flask(__name__) #Flaskインスタンスをappで宣言
Bootstrap = Bootstrap(app)

# @...デコレータ、真下の行の関数を引数にとる
# 呼び出し自体は真下の行の関数でおｋ、実行自体はデコレータが実行される
@app.route("/") #「/」へアクセスしたとき
@app.route("/index") #「/index」にアクセスしたとき
def index():
    print("def index")
    name = request.args.get("name")
    all_onegai = OnegaiContent.query.all() # SELECT ** FROM XX

    return render_template("index.html",name=name,all_onegai=all_onegai) # index.htmlで使えるようになる

@app.route("/index", methods=["post"]) #htmlのformactionの名前が/indexで、POSTを受け取ったとき
def post():
    print("def post index")
    name = request.form["name"] # index.htmlのフォームのname指定した変数をnameに代入
    all_onegai = OnegaiContent.query.all() # SELECT ** FROM XX
    # [<Title 'fdsaf'>, <Title 'っっっっっっｆ'>, <Title 'aaa'>] DBをリスト構造で全て出力された結果
    return render_template("jmap_test.html",name=name,all_onegai=all_onegai) # index.htmlで使えるようになる

@app.route("/add", methods=["post"]) # htmlのformactionの名前が/addからpostを受け取った時
def add():
    print("def add")
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content) # db_session... データベース接続用のインスタンス、database.pyで宣言してる
    db_session.commit()
    return index() # returnに関数渡すこともできる

@app.route("/update",methods=["post"]) # htmlのformactionの名前がupdate
def update():
    print("def update")
    print(request.form) # ImmutableMultiDict([('title', 'fff'), ('body', 'fffdsa'), ('update', '5')])
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index() # この後にindex()も実行するので、db表示される

@app.route("/delete",methods=["post"])
def delete():
    print("def delete")
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

if __name__ == "__main__":
    app.run(debug=True)
