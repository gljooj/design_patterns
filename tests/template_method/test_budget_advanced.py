import unittest

from design_patterns.budget.budgets.budget_advanced import BudgetAdvanced, Item
from design_patterns.budget.calculators.calc_discounts import CalcDiscounts
from design_patterns.budget.taxation.taxes import ICPPTaxesTypeCalc, IKCVTaxesTypeCalc


class TestBudgetAdvanced(unittest.TestCase):

    def test_budget_advanced(self):
        budget = BudgetAdvanced()
        budget.add_items(Item(name='Item 1', price=100))
        budget.add_items(Item(name='Item 2', price=200))
        budget.add_items(Item(name='Item 3', price=300))

        calculator = CalcDiscounts(budget)
        icpp = ICPPTaxesTypeCalc()
        ikcv = IKCVTaxesTypeCalc()

        icpp_calc = calculator.do_calc(icpp)
        ikcv_calc = calculator.do_calc(ikcv)
        final_price = budget.price - icpp_calc - ikcv_calc

        print(final_price)
        assert final_price < budget.price
