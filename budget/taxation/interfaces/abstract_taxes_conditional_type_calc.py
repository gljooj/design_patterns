import abc

from budget.budgets.budget_advanced import BudgetAdvanced
from budget.taxation.services.taxes_next_taxes_service import TaxesNextTaxesService


class AbstractTaxesConditionalTypeCalc(TaxesNextTaxesService):
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
