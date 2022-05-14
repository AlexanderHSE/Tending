import ApiParsing
from HelpFunc import HelpFunc
import Analytics
import tinkoff


class Portfolio:
    __slots__ = ('__id', '__port_name', '__account', '__analytics', '__accounts')

    # Получаем id аккаунта
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, _id):
        self.__id = _id

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

    def get_one_acc(self):
        if (len(self.__accounts)) == 1:
            self.__account = self.__accounts[0].name
        else:
            names = [acc.name for acc in self.__accounts if acc.status == 2 and 1 == acc.type]
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
            self.id = self.__accounts[choice - 1].id
            self.port_name = self.__accounts[choice - 1].name

    def rename_port(self, new_name):
        self.port_name = new_name

    def get_analytics(self):
        if self.account:
            self.__analytics = Analytics.Analytics()

    def __init__(self, accounts):
        self.__accounts = accounts
        self.__id = None
        self.__analytics = None
        self.__account = None
        self.__port_name = None
