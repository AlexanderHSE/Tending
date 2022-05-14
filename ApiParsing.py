from tinkoff.invest import Client, GetAccountsResponse, RequestError
from tinkoff.invest.services import Services


class ApiParsing:
    __slots__ = ('__token', '__accounts')

    # Получаем токен
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, _token):
        self.__token = _token

    def input_token(self):
        print("Введите токен")
        self.token = input()

    # Получаем доступ к аккаунту
    def get_accounts(self):
        while True:
            self.input_token()
            try:
                with Client(self.token) as client:
                    self.__accounts = client.users.get_accounts()
                    break
            except RequestError:
                print("Have not success!")

    @property
    def accounts(self):
        return self.__accounts

    def __init__(self):
        self.__token = None
        self.__accounts = None
