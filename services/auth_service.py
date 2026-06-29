import bcrypt
from database.mongodb import mongodb


class AuthService:

    @staticmethod
    def login(username, password, role):

        db = mongodb.get_database()

        print("Database:", db)

        user = db.users.find_one(
            {
                "username": username,
                "role": role,
                "status": "Active"
            }
        )

        print("User Found:", user)

        if user is None:
            return False

        print("Stored Password:", user["password"])
        print("Entered Password:", password)

        result = bcrypt.checkpw(
            password.encode("utf-8"),
            user["password"]
        )

        print("Password Match:", result)

        return result