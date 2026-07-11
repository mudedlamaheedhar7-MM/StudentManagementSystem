from services.fee_service import FeeService


class FeeController:

    # ------------------------------------------
    # CREATE FEE
    # ------------------------------------------

    @staticmethod
    def save_fee(fee):
        return FeeService.create_fee(fee)

    # ------------------------------------------
    # GET ALL FEES
    # ------------------------------------------

    @staticmethod
    def get_all_fees():
        return FeeService.get_all_fees()

    # ------------------------------------------
    # GET FEE BY ID
    # ------------------------------------------

    @staticmethod
    def get_fee_by_id(fee_id):
        return FeeService.get_fee_by_id(fee_id)

    # ------------------------------------------
    # GET FEES BY STUDENT
    # ------------------------------------------

    @staticmethod
    def get_fees_by_student(student_id):
        return FeeService.get_fees_by_student(student_id)

    # ------------------------------------------
    # UPDATE FEE
    # ------------------------------------------

    @staticmethod
    def update_fee(fee):
        return FeeService.update_fee(fee)

    # ------------------------------------------
    # DELETE FEE
    # ------------------------------------------

    @staticmethod
    def delete_fee(fee_id):
        return FeeService.delete_fee(fee_id)

    # ------------------------------------------
    # SEARCH FEES
    # ------------------------------------------

    @staticmethod
    def search_fees(keyword):
        return FeeService.search_fees(keyword)

    # ------------------------------------------
    # GENERATE FEE ID
    # ------------------------------------------

    @staticmethod
    def generate_fee_id():
        return FeeService.generate_fee_id()