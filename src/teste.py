# def get_database():
#     from pymongo import MongoClient
#     import pymongo


#     client  = MongoClient(CONNECTION_STRING)

#     return client["NFSe"]

# dbname      = get_database()
# collection  = dbname["Tags"]
# details     = collection.find()
# for item in details:
#     print(item["COD_CIDADE"])
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("Teste"))