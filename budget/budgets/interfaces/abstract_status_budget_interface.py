import abc

from budget.discounts.interfaces.abstract_discount_type_calc import AbstractDiscountTypeCalc


class AbstractStatusBudgetInterface(AbstractDiscountTypeCalc):
    def __init__(self):
        self.discounted = False

    @abc.abstractmethod
    def approve(self, budget):
        pass

    @abc.abstractmethod
    def disapprove(self, budget):
        pass

    @abc.abstractmethod
    def type_calc(self, budget):
        pass

    @abc.abstractmethod
    def finish(self, budget):
        pass
