from budget.budgets.budget_advanced import BudgetAdvanced
from budget.discounts.interfaces.abstract_discount_type_calc import AbstractDiscountTypeCalc


class verifyDiscount(AbstractDiscountTypeCalc):
    def type_calc(self, budget: BudgetAdvanced):
        return ItemDiscountTypeCalc().type_calc(budget)


class ItemDiscountTypeCalc(AbstractDiscountTypeCalc):
    def type_calc(self, budget: BudgetAdvanced):
        if budget.total_items > 5:
            return budget.price * 0.1
        return DiscountPerPrice().type_calc(budget)


class DiscountPerPrice(AbstractDiscountTypeCalc):
    def type_calc(self, budget: BudgetAdvanced):
        if budget.price > 500:
            return budget.price * 0.07
        return 0
