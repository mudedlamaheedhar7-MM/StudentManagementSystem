from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME


class MongoDB:
    def __init__(self):
        self.client = None
        self.database = None

    def connect(self):
        """Connect to MongoDB only once."""
        if self.database is not None:
            return self.database

        try:
            self.client = MongoClient(MONGO_URI)
            self.client.admin.command("ping")  # Test connection

            self.database = self.client[DATABASE_NAME]

            print("✅ MongoDB Connected Successfully.")

        except Exception as error:
            print("❌ Database Connection Error")
            print(error)

        return self.database

    def get_database(self):
        """Return the database. Connect automatically if needed."""
        if self.database is None:
            self.connect()

        return self.database


# Singleton instance
mongodb = MongoDB()
