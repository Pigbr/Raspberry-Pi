from pymongo import MongoClient

# 連線 MongoDB
mongo_uri = "你的token  e.g. mongodb+srv://pi_user:<db_password>@cluster0.qtdvfci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)

# 指定資料庫
db = client["mydatabase"]
collection = db["mycollection"]

person = collection.find_one({"name": "Alice"})
print("查到的資料：", person)