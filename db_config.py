import datetime
import os
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField, TimestampField

# import logging

# .envの読み込み
load_dotenv()

db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合

if not db.connect():
    print("接続NG")
    exit()


class users_list(Model):
    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    age = IntegerField()
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:  # データベースアクセスに関連する追加の情報や機能を差し挟んでくれる
        database = db
        table_name = "user_info"


db.create_tables([users_list])
