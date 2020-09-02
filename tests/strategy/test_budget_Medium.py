from design-patterns.budget.budgets.budget_medium import BudgetMedium
from design-patterns.budget.calculators.calc_taxes import CalcTaxes
from design-patterns.budget.taxation.icms_taxes_type_calc import IcmsTaxesTypeCalc
import unittest

from design-patterns.budget.taxation.iss_taxes_type_calc import IssTaxesTypeCalc


class TestBudgetMedium(unittest.TestCase):

    def test_budget_medium(self):
        # test budget Medium
        budget = BudgetMedium(500)
        calculator = CalcTaxes(budget)
        icms = IcmsTaxesTypeCalc()
        iss = IssTaxesTypeCalc()

        do_calc = calculator.do_calc(icms)
        final_price = do_calc + budget.price

        print(final_price)
        assert final_price is not None
