from budget.budgets.budget_medium import BudgetMedium
from budget.taxation.interfaces.abstract_taxes_conditional_type_calc import \
    AbstractTaxesConditionalTypeCalc
from budget.taxation.interfaces.abstract_taxes_type_calc import AbstractTaxesTypeCalc


# PYTHON DECORATOR, it takes a function or method and do other action.
def IPVX(function_or_method):
    def wrapper(self, budget):
        return function_or_method(self, budget) + 50.0

    return wrapper


class IssTaxesTypeCalc(AbstractTaxesTypeCalc):
    @IPVX
    def type_calc(self, budget):
        return budget.price * 0.1 + self.calc_next_taxe(budget)


class IcmsTaxesTypeCalc(AbstractTaxesTypeCalc):
    def type_calc(self, budget):
        return budget.price * 0.6 + self.calc_next_taxe(budget)


class ICPPTaxesTypeCalc(AbstractTaxesConditionalTypeCalc):

    def verify_taxation(self, budget):
        if budget.price > 500:
            return self.maximum_taxation(budget) + self.calc_next_taxe(budget)
        else:
            return self.minimum_taxation(budget) + self.calc_next_taxe(budget)

    def maximum_taxation(self, budget):
        return budget.price * 0.07

    def minimum_taxation(self, budget):
        return budget.price * 0.05


class IKCVTaxesTypeCalc(AbstractTaxesConditionalTypeCalc):
    def verify_taxation(self, budget):
        if budget.price > 500 and self.__has_item_more_than_100_reais(budget):
            return self.maximum_taxation(budget) + self.calc_next_taxe(budget)
        else:
            return self.minimum_taxation(budget) + self.calc_next_taxe(budget)

    def maximum_taxation(self, budget):
        return budget.price * 0.1

    def minimum_taxation(self, budget):
        return budget.price * 0.06

    def __has_item_more_than_100_reais(self, budget):
        for item in budget.get_items():
            if item.price > 100:
                return True
        return False
