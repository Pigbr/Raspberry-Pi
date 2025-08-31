from pymongo import MongoClient

# 連線 MongoDB
mongo_uri = "你的token  e.g. mongodb+srv://pi_user:<db_password>@cluster0.qtdvfci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)

# 指定資料庫
db = client["mydatabase"]
collection = db["mycollection"]
doc = {"name": "Alice", "age": 25}
result = collection.insert_one(doc)
print("插入單筆資料的 ID：", result.inserted_id)

# 列出資料庫下的所有集合
collections = db.list_collection_names()
print("目前資料庫下的 Collections：")
for col in collections:
    print("-", col,"\n")
