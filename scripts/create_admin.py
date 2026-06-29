from pymongo import MongoClient
import bcrypt

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student_management_system"]

# Users collection
users = db["users"]

# Default admin credentials
username = "admin"
password = "admin123"

# Check if admin already exists
existing_user = users.find_one({"username": username})

if existing_user:
    print("✅ Admin user already exists.")
else:
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users.insert_one({
        "username": username,
        "password": hashed_password,
        "role": "Admin",
        "status": "Active"
    })

    print("✅ Admin user created successfully!")