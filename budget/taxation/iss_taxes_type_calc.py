from design_patterns.budget.budgets.budget_medium import BudgetMedium
from design_patterns.budget.taxation.interfaces.abstract_taxes_type_calc import AbstractTaxesTypeCalc


class IssTaxesTypeCalc(AbstractTaxesTypeCalc):
    def type_calc(self, budget: BudgetMedium):
        return budget.price * 0.1
