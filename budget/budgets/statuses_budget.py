from design_patterns.budget.budgets.interfaces.abstract_status_budget_interface import AbstractStatusBudgetInterface


class StatusesBudget:
    class Analyze(AbstractStatusBudgetInterface):
        def type_calc(self, budget):
            if not self.discounted:
                budget.add_extra_discount(budget.price * 0.02)
                self.discounted = True
            else:
                raise Exception("Discound is already Approved")

        def approve(self, budget):
            budget.actual_status = StatusesBudget.Approved()

        def desapprove(self, budget):
            budget.actual_status = StatusesBudget.Desapproved()

        def finish(self, budget):
            raise Exception("Status must be desapproved or approved to be Finished")

    class Approved(AbstractStatusBudgetInterface):
        def type_calc(self, budget):
            if not self.discounted:
                budget.add_extra_discount(budget.price * 0.05)
                self.discounted = True
            else:
                raise Exception("Discound is already Approved")

        def approve(self, budget):
            raise Exception("Status is already Approved")

        def desapprove(self, budget):
            raise Exception("Budgets approved can not be Desapproved")

        def finish(self, budget):
            budget.actual_status = StatusesBudget.Fineshed()

    class Desapproved(AbstractStatusBudgetInterface):
        def type_calc(self, budget):
            raise Exception("Desapproved budget do not receive Discount")

        def approve(self, budget):
            budget.actual_status = StatusesBudget.Approved()

        def desapprove(self, budget):
            raise Exception("Status is already Desapproved")

        def finish(self, budget):
            budget.actual_status = StatusesBudget.Fineshed()

    class Fineshed(AbstractStatusBudgetInterface):
        def type_calc(self, budget):
            raise Exception("Fineshed budget can not receive Discount")

        def approve(self, budget):
            raise Exception("Fineshed budget can not be Approved")

        def desapprove(self, budget):
            raise Exception("Fineshed budget can not be Desapproved")

        def finish(self, budget):
            raise Exception("Fineshed budget do not receive discount")
