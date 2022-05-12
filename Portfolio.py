from tinkoff.invest import Client, GetAccountsResponse, RequestError
from tinkoff.invest.services import Services
class Portfolio:
    token = None
    accounts = None
    def __get_token(self) -> str:
        """
        Получение токена.
        :return: Получает токен.
        """
        token = input()
        return token

    def get_accounts(self, token : str) -> GetAccountsResponse:
        """
        Получить массив счетов клиента.
        :param token: Токен клиента.
        :return: Массив счетов клиента.
        """
        client: Services
        try:
            with Client(token) as client:
                return client.users.get_accounts()
        except RequestError:
            return None
            print("error!")

    def __init__(self):
        self.token = self.__get_token(self)
        self.accounts = self.get_accounts(self.token)
