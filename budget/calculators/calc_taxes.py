from budget.calculators.interfaces.abstract_calculator_medium import AbstractCalculatorMedium
from budget.taxation.interfaces.abstract_taxes_type_calc import AbstractTaxesTypeCalc


class CalcTaxes(AbstractCalculatorMedium):
    def __init__(self, budget):
        self.budget = budget

    def do_calc(self, calc: AbstractTaxesTypeCalc):
        return calc.type_calc(self.budget)
