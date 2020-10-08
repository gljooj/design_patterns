import unittest

from design_patterns.budget.budgets.budget_advanced import BudgetAdvanced, Item
from design_patterns.budget.budgets.statuses_budget import StatusesBudget as Statuses
from design_patterns.budget.calculators.calc_discounts import CalcDiscounts
from design_patterns.budget.taxation.taxes import ICPPTaxesTypeCalc, IKCVTaxesTypeCalc


class TestBudgetAdvanced(unittest.TestCase):

    def test_status(self):
        budget = BudgetAdvanced()
        budget.add_items(Item(name='Item 1', price=100))
        budget.add_items(Item(name='Item 2', price=200))
        budget.add_items(Item(name='Item 3', price=300))

        budget.approve()
        budget.get_extra_discount()
        calculator = CalcDiscounts(budget)
        final_price = budget.price

        print(final_price)
