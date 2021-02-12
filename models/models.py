from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

# テーブル定義, テーブルのデータの変数名を決めたりする
class OnegaiContent(Base):# DB接続情報とテーブル定義を紐付け
    # テーブルからのデータの受け取りはこのクラスで
    __tablename__ = "onegaicontents"

    id = Column(Integer, primary_key=True)

    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title=title
        self.body = body
        self.date = date

    def __repr__(self):
        return "<Title %r>" % (self.title)