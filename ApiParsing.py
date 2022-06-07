from tinkoff.invest import Client, RequestError


class ApiParsing:
    __slots__ = ('__token', '__accounts')

    def __init__(self):
        self.__token = None
        self.__accounts = None

    # Получаем токен
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, _token):
        self.__token = _token

    # Получаем доступ к аккаунту
    def get_accounts(self, token):
        while True:
            self.token(token)
            try:
                with Client(self.token) as client:
                    self.__accounts = client.users.get_accounts()
                    break
            except RequestError:
                print("Have not success!")

    @property
    def accounts(self):
        return self.__accounts


