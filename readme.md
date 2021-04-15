# URL
https://testflask-app-hiroki.herokuapp.com/

# Todo
- [x] データ撮ってくる
- [x] NHKクレジット表記
- [x] covid割合でヒートマップ
- [x] 完治者数と死亡者の割合表示
- [x] ~heroku~ Github Actionsで自動データ取得、更新
- [x] mac, iphone chrome で県をクリックするたび円グラフが倍の大きさになるバグ潰す
- [ ] 陽性者のうち、完治した人を追加する(データない?)
- [ ] そもそもFlask使う必要性がない(CSV読む-> JSでできる、ルーティングも何も必要がない、データ取得はrequestでFlask関係ない)
- [ ] 会員登録制、住所によってLINE通知を送る

# できること
+ WebページからDBの編集、読み込み
+ URL変えずに内容変更
+ かんたんJQuery
+ jmap設置
+ JSONファイルの読み込み
+ かんたんGithub Actions

# 構成
+ Flask--gunicorn(WSGIサーバ？)--Heroku(Webサーバ)(Githubと連携させてる)
+ bootstrap
+ JQuery
+ jmap
+ Github Actions

# herokuについて
## 準備
以下の全コマンドはGit管理してる親フォルダでやる

必要なパッケージ(以下はHerokuでFlask動かすために最低必要)インストール
```
pip install Flask gunicorn
```

requirements.txtを生成
```
pip freeze > requirements.txt
```
同じ階層にアプリ起動時の処理を書くProcfile生成
```
web: gunicorn run:app --log-file=-
```
これの意味
+ Procfile
```
<process type>: <command>
```
の形で定義する。
タイプwebだけは特別であり、herokuからのHTTPトラフィックがルーティングされる模様。 他は任意。（https://devcenter.heroku.com/articles/procfile）
+ --log-file=-
標準エラー出力にログを出力（現在はデフォルトでこれなのでなくてよい）
+ gunicorn
WSGIサーバーの名前(他のWSGIサーバーはuWSGI, waitressなど)  
WSGI...Webアプリとサーバーをつなぐ仕様、汎用的なインターフェイスの定義. Flaskの場合
```
app = Flask(...)
```
とかくが、app自体がWSGIアプリケーションとなる。
Flask, Django, ZopeなどのFWで利用されている.

> WSGIアプリケーションの仕様をまとめると
> - 2つの引数を持った呼び出し可能なオブジェクト
> - 第2引数として渡されたオブジェクトにHTTPステータスコードと[(レスポンスヘッダ, 値)]という値を渡して呼び出す
> - 返り値にiterable objectを返す
> - 返り値のiterableをiterateすると，文字列を返す  
> 引用元(https://gihyo.jp/dev/feature/01/wsgi/0001?page=2)

## heroku作業
heroku CLIインスコする

コマンドプロンプトでherokuログイン
```
heroku login
```

アプリケーション作成
```
heroku create アプリケーション名
```
「heroku」リモートリポジトリ生成される

herokuデプロイ(「heroku」リモートリポジトリにpushするだけ、すごい)
```
git push heroku master
```

確認
```
heroku open
```

# ファイル説明
### run.py
注意点:
herokuにアップするには、IPを0.0.0.0固定の必要がある。


# 参考
+ https://qiita.com/kiyokiyo_kzsby/items/0184973e9de0ea9011ed
+ https://mickey-happygolucky.hatenablog.com/entry/2018/03/29/012822
+ https://yugokimura.github.io/jmap/#quickstart
+ https://mycodingjp.blogspot.com/2018/11/python-flask-javascript.html
+ https://www.youtube.com/watch?v=T0KAE2kq2Xo
+ https://www.mathpython.com/ja/flask-favicon/
+ https://ao-system.net/alphaicon/
