try:
    import pymongo
    print("✅ pymongo 已經安裝！")
except ImportError:
    print("❌ pymongo 未安裝，請先安裝：pip install pymongo")
    exit(1)

# 測試能否連線到 MongoDB
# 替換下面 URI 為你的 MongoDB Atlas 或本地 MongoDB
mongo_uri = "你的token  e.g. mongodb+srv://pi_user:<db_password>@cluster0.qtdvfci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = pymongo.MongoClient(mongo_uri)
    # 嘗試列出資料庫
    dbs = client.list_database_names()
    print("✅ 成功連線到 MongoDB！")
    print("現有資料庫：", dbs)
except Exception as e:
    print("❌ 無法連線到 MongoDB")
    print("錯誤訊息：", e)
