from rest_framework import exceptions

from core.third_party_api.otkrytie_api import OtkrytieAPI


otkrytie_api = OtkrytieAPI()


def verify_user(jwt_token: str) -> bool | Exception:
    response = otkrytie_api.verification(jwt_token)

    if 'userId' in response.keys():
        return True

    raise exceptions.AuthenticationFailed(response)
