import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
import json

class MongoConnector():
    def __init__(self) -> None:
        load_dotenv()
        CONNECTION_STRING   = getenv("CONNECTION_STRING")
        self.client = MongoClient(CONNECTION_STRING)
        self.client = self.client["NFSe"]
    
    def get_data(self):
        self.collection = self.client["Tags"]
        self.details    = self.collection.find({}, {'_id': False})
        return {row["COD_CIDADE"]: row for row in self.details}