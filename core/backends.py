from django.conf import settings

from rest_framework import authentication, exceptions

from core.utils.verification_utils import verify_user
from core.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(token)

    @staticmethod
    def _authenticate_credentials(token):
        user_data = verify_user(token)

        user = User.objects.get_or_create(**user_data)

        return user
