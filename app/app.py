# アプリの動き(変数？)を書くところらしい

#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request,send_from_directory
from flask_bootstrap import Bootstrap

from datetime import datetime

import csv
import os

app = Flask(__name__) #Flaskインスタンスをappで宣言
Bootstrap = Bootstrap(app)

# @...デコレータ、真下の行の関数を引数にとる
# 呼び出し自体は真下の行の関数でおｋ、実行自体はデコレータが実行される
@app.route("/") #「/」へアクセスしたとき
def index():
    # 人口取得 now_covids=now_covids
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/csv/nhk_news_covid19_prefectures_daily_data.csv")
    print(path)

    csvfile = open(path,encoding="utf-8")
    prefnames = {} # {"県名": [コロナ合計感染者数, 死亡者数]}
    for index, row in enumerate(csv.reader(csvfile)):
        if index == 0:
            continue
        row_prefname = row[2]
        row_covid_total_num = int(row[4])
        row_covid_total_dead = int(row[6])

        prefnames[row_prefname] = [row_covid_total_num, row_covid_total_dead]


    # ここで現在の感染者数と、人口を渡す
    return render_template("index.html", pref_covid_total_dict=prefnames) # index.htmlで使えるようになる

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico', )