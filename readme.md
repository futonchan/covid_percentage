# できること
+ WebページからDBの編集、読み込み
+ URL変えずに内容変更
+ かんたんJQuery
+ jmap設置

# 構成
Flask--gunicorn(WSGI)--Heroku(Webサーバ)
bootstrap
JQuery
jmap

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

# 参考
https://qiita.com/kiyokiyo_kzsby/items/0184973e9de0ea9011ed