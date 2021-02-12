from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# DB接続情報
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'onegai.db') # dbファイル
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True) # SQLiteで、dbファイルのパスにDB構築
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine)) # DB接続用のインスタンス
Base = declarative_base() # Baseオブジェクト
Base.query = db_session.query_property() # BaseのクエリにDBの情報入れる


def init_db(): # DB初期化
    import models.models
    Base.metadata.create_all(bind=engine) # テーブル作成