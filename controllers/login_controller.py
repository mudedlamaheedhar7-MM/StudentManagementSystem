from services.auth_service import AuthService


class LoginController:

    @staticmethod
    def authenticate(username, password, role):

        return AuthService.login(
            username,
            password,
            role
        )