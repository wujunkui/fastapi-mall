import jwt
import logging


class UserService:

    @staticmethod
    def verify_token(token: str) -> bool:
        try:
            jwt.decode(token)
        except Exception as e:
            logging.warning(e)
            return False
        return True

    @staticmethod
    def create_user():
        pass

    @staticmethod
    def get_user_by_email(email: str):
        pass

    @staticmethod
    def get_user_by_token(token: str):
        pass
