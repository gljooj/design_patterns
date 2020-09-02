from design_patterns.budget.budgets.budget_medium_with_discount import BudgetMediumWithDiscount
from design_patterns.budget.discounts.interfaces.abstract_discount_type_calc import AbstractDiscountTypeCalc


class verifyDiscount(AbstractDiscountTypeCalc):
    def type_calc(self, budget: BudgetMediumWithDiscount):
        return ItemDiscountTypeCalc().type_calc(budget)


class ItemDiscountTypeCalc(AbstractDiscountTypeCalc):
    def type_calc(self, budget: BudgetMediumWithDiscount):
        if budget.total_items > 5:
            return budget.price * 0.1
        return DiscountPerPrice().type_calc(budget)


class DiscountPerPrice(AbstractDiscountTypeCalc):
    def type_calc(self, budget: BudgetMediumWithDiscount):
        if budget.price > 500:
            return budget.price * 0.07
        return 0
