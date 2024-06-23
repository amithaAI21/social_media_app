from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

UserModel = get_user_model()
username_validator = UnicodeUsernameValidator()

class CaseInsensitiveEmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return

        # Normalize the email before lookup
        email = UserModel.objects.normalize_email(email)

        # Case-insensitive lookup for email
        user = UserModel.objects.filter(email__iexact=email).first()

        if user and user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
