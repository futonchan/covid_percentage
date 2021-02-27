import urllib.request

# ダウンロードするやつ init
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0")]
urllib.request.install_opener(opener)

dataurl = "https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv"
urllib.request.urlretrieve(dataurl, "./app/static/csv/nhk_news_covid19_prefectures_daily_data.csv")