import unittest

from budget.budgets.budget_advanced import BudgetAdvanced, Item
from budget.calculators.calc_discounts import CalcDiscounts
from budget.discounts.discounts import verifyDiscount


class TestBudgetAdvanced(unittest.TestCase):

    def test_budget_advanced_with_discount(self):
        budget = BudgetAdvanced()
        budget.add_items(Item(name='Item 1', price=100))
        budget.add_items(Item(name='Item 2', price=200))
        budget.add_items(Item(name='Item 3', price=300))

        calculator = CalcDiscounts(budget)
        verify_discount = verifyDiscount()

        discount = calculator.do_calc(verify_discount)
        final_price = budget.price - discount
        print(final_price)
        assert final_price < budget.price
        assert discount > 0.0
