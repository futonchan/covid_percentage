# Todo
- [x] データ撮ってくる
- [x] NHKクレジット表記
- [x] covid割合でヒートマップ
- [x] 完治者数と死亡者の割合表示
- [ ] herokuで自動データ取得


# できること
+ WebページからDBの編集、読み込み
+ URL変えずに内容変更
+ かんたんJQuery
+ jmap設置
+ JSONファイルの読み込み

# 構成
+ Flask--gunicorn(WSGI)--Heroku(Webサーバ)
+ bootstrap
+ JQuery
+ jmap

# herokuについて
## 準備
以下の全コマンドはGit管理してる親フォルダでやる

requirements.txtを生成
```
pip freeze > requirements.txt
```
同じ階層にアプリ起動時の処理を書くProcfile生成
```
web: gunicorn run:app --log-file=-
```

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
https://qiita.com/kiyokiyo_kzsby/items/0184973e9de0ea9011ed
https://mickey-happygolucky.hatenablog.com/entry/2018/03/29/012822
https://yugokimura.github.io/jmap/#quickstart
https://mycodingjp.blogspot.com/2018/11/python-flask-javascript.html
