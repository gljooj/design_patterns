import unittest

from design_patterns.budget.budgets.budget_medium_with_discount import BudgetMediumWithDiscount, Item
from design_patterns.budget.calculators.calc_discounts import CalcDiscounts
from design_patterns.budget.discounts.discounts import verifyDiscount


class TestBudgetMediumWithDiscount(unittest.TestCase):

    def test_budget_medium_with_discount(self):
        budget = BudgetMediumWithDiscount()
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
