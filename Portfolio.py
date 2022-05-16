import ApiParsing
from HelpFunc import HelpFunc
import Analytics
import tinkoff


class Portfolio:
    __slots__ = ('__port_name', '__account', '__analytics', '__accounts', '__token')

    # Получаем название аккаунта
    @property
    def port_name(self):
        return self.__port_name

    @port_name.setter
    def port_name(self, _port_name):
        self.__port_name = _port_name

    # Получаем счет аккаунта
    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, _account):
        self.__account = _account

    # Получаем токен
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, _token):
        self.__token = _token

    # Получаем аналитику
    @property
    def analytics(self):
        return self.__analytics

    @analytics.setter
    def analytics(self, _analytics):
        self.__analytics = _analytics


    def get_one_acc(self):
        if (len(self.__accounts)) == 1:
            if self.__accounts[0].status == 2 and 1 == self.__accounts[0].type:
                self.account = self.__accounts[0].name
                self.port_name = self.__accounts[0].name
            else:
                print("no on can be added")
        else:
            names = [acc.name for acc in self.__accounts if acc.status == 2 and 1 == acc.type]
            if len(names):
                print("Какой брокерский счет добавлять")
                for i in range(len(names)):
                    print(f"{i + 1}  {names[i]}")
                choice = HelpFunc.Input_number(1, len(names))
                name_choice = names[choice - 1]
                acc = None
                for enum_acc in self.__accounts:
                    if enum_acc.name == name_choice:
                        acc = enum_acc
                        break
                self.account = acc
                self.port_name = self.__accounts[choice - 1].name
            else:
                print("no on can be added")

    def rename_port(self, new_name):
        self.port_name = new_name

    def get_analytics(self):
        if self.account:
            self.analytics = Analytics.Analytics(self.account, self.token)
            self.analytics.create_df()

    def __init__(self, accounts, token):
        self.__accounts = accounts
        self.__analytics = None
        self.__account = None
        self.__port_name = None
        self.__token = token
