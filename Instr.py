from tinkoff.invest import Client,InstrumentIdType


class Instr:
    __slots__ = ('__client', '__figi', '__instrument')

    def __init__(self, token, figi, instr_type):
        with Client(token) as client:
            if instr_type == 'bond':
                self.instr = client.instruments.bond_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                        id=figi).instrument
            elif instr_type == 'share':
                self.instr = client.instruments.share_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                         id=figi).instrument
            elif instr_type == 'etf':
                self.instr = client.instruments.etf_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                       id=figi).instrument
            elif instr_type == 'currency':
                self.instr = client.instruments.currency_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                            id=figi).instrument
            elif instr_type == 'futures ':
                self.instr = client.instruments.future_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                          id=figi).instrument

    # Получаем client
    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, _client):
        self.__client = _client

    # Получаем figi
    @property
    def figi(self):
        return self.__figi

    @figi.setter
    def figi(self, _figi):
        self.__figi = _figi

    # Получаем instr
    @property
    def instr(self):
        return self.__instrument

    @instr.setter
    def instr(self, _instrument):
        self.__instrument = _instrument
