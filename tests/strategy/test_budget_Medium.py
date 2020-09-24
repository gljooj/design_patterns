import unittest

from design_patterns.budget.budgets.budget_medium import BudgetMedium
from design_patterns.budget.calculators.calc_taxes import CalcTaxes
from design_patterns.budget.taxation.taxes import IcmsTaxesTypeCalc, IssTaxesTypeCalc


class TestBudgetMedium(unittest.TestCase):

    def test_budget_medium(self):
        # test budget Medium
        budget = BudgetMedium(500)
        calculator = CalcTaxes(budget)
        icms = IcmsTaxesTypeCalc()
        iss = IssTaxesTypeCalc()

        icms_calc = calculator.do_calc(icms)
        iss_calc = calculator.do_calc(iss)
        final_price = icms_calc + iss_calc + budget.price

        print("final price", final_price)
        assert final_price is not None
