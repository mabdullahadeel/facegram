from facegram.users.models import User


class UserResponse:
    
    @staticmethod
    def get_user_payload(user: User):
        return {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id,
            "tokens": user.get_tokens()
        }