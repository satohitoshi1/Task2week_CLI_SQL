from db_config import users_list

message = users_list(name="Bob", age="15")  # pub_dateはデフォルト値を指定したので省略できる
message.save()
