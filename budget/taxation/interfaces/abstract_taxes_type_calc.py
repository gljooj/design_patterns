import abc

from design_patterns.budget.taxation.services.taxes_next_taxes_service import TaxesNextTaxesService


class AbstractTaxesTypeCalc(TaxesNextTaxesService):
    @abc.abstractmethod
    def type_calc(self, BudgetMedium):
        raise NotImplementedError
