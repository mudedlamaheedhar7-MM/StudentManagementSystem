from database.mongodb import mongodb


class FeeService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.fees

    # ------------------------------------------
    # CREATE FEE
    # ------------------------------------------

    @staticmethod
    def create_fee(fee):

        collection = FeeService.get_collection()

        existing = collection.find_one(
            {"fee_id": fee.fee_id}
        )

        if existing:
            return False

        collection.insert_one(
            fee.to_dict()
        )

        return True

    # ------------------------------------------
    # GET ALL FEES
    # ------------------------------------------

    @staticmethod
    def get_all_fees():

        collection = FeeService.get_collection()

        return list(
            collection.find(
                {},
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GET FEE BY ID
    # ------------------------------------------

    @staticmethod
    def get_fee_by_id(fee_id):

        collection = FeeService.get_collection()

        return collection.find_one(
            {"fee_id": fee_id},
            {"_id": 0}
        )

    # ------------------------------------------
    # GET FEES BY STUDENT
    # ------------------------------------------

    @staticmethod
    def get_fees_by_student(student_id):

        collection = FeeService.get_collection()

        return list(
            collection.find(
                {"student_id": student_id},
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # UPDATE FEE
    # ------------------------------------------

    @staticmethod
    def update_fee(fee):

        collection = FeeService.get_collection()

        result = collection.update_one(
            {"fee_id": fee.fee_id},
            {"$set": fee.to_dict()}
        )

        return result.modified_count > 0

    # ------------------------------------------
    # DELETE FEE
    # ------------------------------------------

    @staticmethod
    def delete_fee(fee_id):

        collection = FeeService.get_collection()

        result = collection.delete_one(
            {"fee_id": fee_id}
        )

        return result.deleted_count > 0

    # ------------------------------------------
    # SEARCH FEES
    # ------------------------------------------

    @staticmethod
    def search_fees(keyword):

        collection = FeeService.get_collection()

        query = {
            "$or": [
                {"fee_id": {"$regex": keyword, "$options": "i"}},
                {"student_id": {"$regex": keyword, "$options": "i"}},
                {"student_name": {"$regex": keyword, "$options": "i"}},
                {"course": {"$regex": keyword, "$options": "i"}},
                {"department": {"$regex": keyword, "$options": "i"}},
                {"status": {"$regex": keyword, "$options": "i"}},
                {"remarks": {"$regex": keyword, "$options": "i"}}
            ]
        }

        return list(
            collection.find(
                query,
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GENERATE FEE ID
    # ------------------------------------------

    @staticmethod
    def generate_fee_id():

        collection = FeeService.get_collection()

        last = collection.find_one(
            {},
            sort=[("fee_id", -1)]
        )

        if not last:
            return "FEE0001"

        number = int(
            last["fee_id"].replace(
                "FEE",
                ""
            )
        )

        number += 1

        return f"FEE{number:04d}"