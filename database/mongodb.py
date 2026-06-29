from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_management_system"]

print("MongoDB Connected Successfully!")
from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME


class MongoDB:

    def __init__(self):
        self.client = None
        self.database = None

    def connect(self):
        try:
            self.client = MongoClient(MONGO_URI)

            # Ping the server to ensure connection
            self.client.admin.command("ping")

            self.database = self.client[DATABASE_NAME]

            print("MongoDB Connected Successfully.")

        except Exception as error:
            print("Database Connection Error")
            print(error)

    def get_database(self):
        return self.database


mongodb = MongoDB()