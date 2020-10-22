from design_patterns.invoice.invoice import Invoice


class InvoiceBuilder(object):
    def __init__(self):
        self.__company_name = None
        self.__document = None
        self.__items = None
        self.__emission_date = None
        self.__details = None
        self.__observers = []

    def company_name(self, company_name):
        self.__company_name = company_name
        return self

    def document(self, document):
        self.__document = document
        return self

    def emission_date(self, emission_date):
        self.__emission_date = emission_date
        return self

    def items(self, items):
        self.__items = items
        return self

    def details(self, details):
        self.__details = details
        return self

    def observers(self, observers):
        self.__observers = observers
        return self

    def build(self):
        if self.__company_name is None:
            raise Exception('Company name was not informated')
        if self.__document is None:
            raise Exception('Document was not informated')
        if self.__items is None:
            raise Exception('Items was not informated')
        if len(self.__details) > 40:
            raise Exception('Details length must be less than 40 characters')

        return Invoice(company_name=self.company_name, document=self.__document, items=self.__items,
                       emission_date=self.__emission_date, details=self.__details, observers=self.__observers)
