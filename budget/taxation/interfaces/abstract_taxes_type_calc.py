import abc

from budget.taxation.services.taxes_next_taxes_service import TaxesNextTaxesService


class AbstractTaxesTypeCalc(TaxesNextTaxesService):
    @abc.abstractmethod
    def type_calc(self, BudgetMedium):
        raise NotImplementedError
