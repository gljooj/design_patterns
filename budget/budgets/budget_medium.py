# Budget = Orcamento
class BudgetMedium(object):
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
