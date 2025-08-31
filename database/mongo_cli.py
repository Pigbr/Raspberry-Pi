from pymongo import MongoClient

# ===== 修改這裡：你的 MongoDB 連線字串 =====
uri = "你的token  e.g. mongodb+srv://pi_user:<db_password>@cluster0.qtdvfci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# 預設資料庫與集合
current_db = client["test"]
current_collection = current_db["people"]

def show_main_menu():
    print("\n=== MongoDB 管理工具 ===")
    print(f"📂 當前 DB: {current_db.name}, Collection: {current_collection.name}")
    print("1. 切換資料庫")
    print("2. 切換 Collection")
    print("3. 新增資料 (Insert)")
    print("4. 查詢資料 (Find)")
    print("5. 更新資料 (Update)")
    print("6. 刪除資料 (Delete)")
    print("7. 列出所有 Collection")
    print("8. 離開")
    return input("請選擇操作：")

while True:
    choice = show_main_menu()

    if choice == "1":
        db_name = input("輸入資料庫名稱: ")
        current_db = client[db_name]
        print(f"✅ 已切換到 DB: {db_name}")

    elif choice == "2":
        coll_name = input("輸入 Collection 名稱: ")
        current_collection = current_db[coll_name]
        print(f"✅ 已切換到 Collection: {coll_name}")

    elif choice == "3":
        name = input("輸入名字: ")
        age = int(input("輸入年齡: "))
        doc = {"name": name, "age": age}
        current_collection.insert_one(doc)
        print("✅ 新增成功:", doc)

    elif choice == "4":
        print("📌 查詢結果：")
        for doc in current_collection.find():
            print(doc)

    elif choice == "5":
        name = input("請輸入要更新的名字: ")
        new_age = int(input("輸入新的年齡: "))
        result = current_collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print("✅ 更新成功！")
        else:
            print("⚠️ 找不到資料")

    elif choice == "6":
        name = input("請輸入要刪除的名字: ")
        result = current_collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("✅ 已刪除！")
        else:
            print("⚠️ 找不到資料")

    elif choice == "7":
        print("📂 Collections in DB:", current_db.list_collection_names())

    elif choice == "8":
        print("👋 離開程式")
        break

    else:
        print("❌ 無效選項，請重新輸入")
