from design_patterns.budget.calculators.interfaces.abstract_calculator_medium import AbstractCalculatorMedium
from design_patterns.budget.discounts.interfaces.abstract_discount_type_calc import AbstractDiscountTypeCalc


class CalcDiscounts(AbstractCalculatorMedium):
    def __init__(self, budget):
        self.budget = budget

    def do_calc(self, calc: AbstractDiscountTypeCalc):
        return calc.type_calc(self.budget)

