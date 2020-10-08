# Budget = Orcamento
from .statuses_budget import StatusesBudget as Statuses


class BudgetAdvanced(object):

    def __init__(self):
        self.__items = []
        self.actual_status = Statuses.Analyze()
        self.__extra_discount = 0

    def approve(self):
        self.actual_status.approve(self)

    def desapprove(self):
        self.actual_status.desapprove(self)

    def finish(self):
        self.actual_status.finish(self)

    def get_extra_discount(self):
        self.actual_status.type_calc(self)

    def add_extra_discount(self, discount):
        self.__extra_discount += discount

    @property
    def price(self):
        total = 0.0
        for item in self.__items:
            total += item.price
        return total - self.__extra_discount

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


