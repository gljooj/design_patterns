import unittest

from budget.budgets.budget_advanced import BudgetAdvanced, Item

class TestBudgetAdvanced(unittest.TestCase):

    def test_status(self):
        budget = BudgetAdvanced()
        budget.add_items(Item(name='Item 1', price=100))
        budget.add_items(Item(name='Item 2', price=200))
        budget.add_items(Item(name='Item 3', price=300))

        budget.approve()
        budget.get_extra_discount()
        final_price = budget.price

        print(final_price)
