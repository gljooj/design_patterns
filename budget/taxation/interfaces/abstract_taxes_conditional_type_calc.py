import abc

from design_patterns.budget.budgets.budget_advanced import BudgetAdvanced


class AbstractTaxesConditionalTypeCalc:
    __metaclass__ = abc.ABCMeta

    def type_calc(self, budget: BudgetAdvanced):
        type_taxation = self.verify_taxation(budget)
        return type_taxation

    @abc.abstractmethod
    def verify_taxation(self, budget):
        return not NotImplementedError

    @abc.abstractmethod
    def maximum_taxation(self, budget):
        return not NotImplementedError

    @abc.abstractmethod
    def minimum_taxation(self, budget):
        return not NotImplementedError
