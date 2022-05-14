class Analytics:
    __slots__ = '__account'

    # Получаем счет аккаунта
    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, _account):
        self.__account = _account

    def __init__(self, account):
        self.account = account
