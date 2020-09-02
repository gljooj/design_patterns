# Budget = Orcamento
class BudgetMediumWithDiscount(object):
    def __init__(self):
        self.__items = []

    @property
    def price(self):
        total = 0.0
        for item in self.__items:
            total += item.price
        return total

    def get_items(self):
        return tuple(self.__items)

    @property
    def total_items(self):
        return len(self.__items)

    def add_items(self, item):
        self.__items.append(item)


class Item(object):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name
