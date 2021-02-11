# アプリの動きを書くところらしい

#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request

#Flaskインスタンスをappで宣言
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    text = ["ABC","HIROKI","YANO"]
    return render_template("index.html",name=name,text=text) # index.htmlで使えるようになる

#おまじない
if __name__ == "__main__":
    app.run(debug=True)
