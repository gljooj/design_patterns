from datetime import date


class InvoiceItem(object):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name


class Invoice:
    def __init__(self, company_name, document, items, emission_date=date.today(), details='',
                 observers=[]):
        self.__company_name = company_name
        self.__document = document
        self.__items = items
        self.__emission_date = emission_date
        self.__details = details

        for observer in observers:
            observer(self)

    @property
    def company_name(self):
        return self.__company_name

    @property
    def document(self):
        return self.__document

    @property
    def items(self):
        return self.__items

    @property
    def emission_date(self):
        return self.__emission_date

    @property
    def details(self):
        return self.__details
