import json
import requests


class URL:
    domain = 'https://hack.invest-open.ru'

    authentication = domain + '/auth'
    verification = domain + '/jwt/verify'
    dialog = domain + '/chat/dialog'
    send_message = domain + '/message/send'
    update_message = domain + '/chat/message/update'
    history = domain + '/chat/history'
    user_info = domain + '/user/info'


class OtkrytieAPI:
    url = URL()

    headers = {'Content-Type': 'application/json'}

    def authentication(self, user_login: str, password_hash: str) -> dict:
        payload = dict(login=user_login, password=password_hash, )

        response = requests.request("POST", url=self.url.authentication, headers=self.headers, data=json.dumps(payload))

        return json.loads(response.text)

    def verification(self, jwt_token: str) -> dict:
        payload = dict(jwt=jwt_token)

        response = requests.request("POST", self.url.verification, headers=self.headers, data=json.dumps(payload))

        return json.loads(response.text)

    def get_user_info(self, user_id: int, jwt_token: str) -> dict:
        url = self.url.user_info + f"?userId={user_id}"

        response = requests.request("GET", url=url, headers=self.get_authentication_headers(jwt_token), data="")

        return json.loads(response.text)

    def update_user_info(self, surname: str, name: str, middle_name: str, avatar: str, jwt_token: str) -> dict:
        payload = dict(surname=surname, name=name, middleName=middle_name, avatar=avatar)

        response = requests.request("POST", url=self.url.user_info, headers=self.get_authentication_headers(jwt_token),
                                    data=json.dumps(payload))

        return json.loads(response.text)

    def send_message(self, dialog_id: int, text: str, message_type: str, data: str, media_url: str,
                     jwt_token: str) -> dict:
        payload = dict(dialogId=dialog_id, text=text, messageType=message_type, data=data, mediaUrl=media_url)

        response = requests.request("POST", url=self.url.send_message,
                                    headers=self.get_authentication_headers(jwt_token), data=json.dumps(payload))

        return json.loads(response.text)

    def get_messages_history(self, dialog_id: int, limit: int, timestamp: int, orger: bool, jwt_token: str) -> dict:
        url = self.url.history + f"?timestamp={timestamp}&older={'TRUE' if orger else 'FALSE'}&limit={limit}&dialogId={dialog_id}"

        response = requests.request("GET", url=url, headers=self.get_authentication_headers(jwt_token), data="")

        return json.loads(response.text)

    def get_available_dialog(self, jwt_token: str) -> dict:
        response = requests.request("GET", url=self.url.dialog, headers=self.get_authentication_headers(jwt_token),
                                    data="")

        return json.loads(response.text)

    def change_widget_data(self, message_id: int, data: dict, jwt_token: str) -> dict:
        payload = dict(messageId=message_id, data=data)

        response = requests.request("POST", url=self.url.update_message,
                                    headers=self.get_authentication_headers(jwt_token), data=json.dumps(payload))

        return json.loads(response.text)

    def get_authentication_headers(self, jwt_token: str) -> dict:
        authentication_headers = self.headers.copy()
        authentication_headers['Authorization'] = f'Bearer {jwt_token}'

        return authentication_headers
