import unittest
from design_patterns.budget.budgets.budget_advanced import BudgetAdvanced, Item
from design_patterns.budget.calculators.calc_taxes import CalcTaxes
from design_patterns.budget.taxation.taxes import ICPPTaxesTypeCalc, IKCVTaxesTypeCalc, IcmsTaxesTypeCalc, \
    IssTaxesTypeCalc


class TestBudgetAdvanced(unittest.TestCase):
    def test_budget_advanced_next_taxes(self):
        budget = BudgetAdvanced()
        budget.add_items(Item(name='Item 1', price=100))
        budget.add_items(Item(name='Item 2', price=200))
        budget.add_items(Item(name='Item 3', price=300))

        calculator = CalcTaxes(budget)

        iss_with_icms = calculator.do_calc(IssTaxesTypeCalc(IcmsTaxesTypeCalc()))
        icpp_with_ikcv = calculator.do_calc(ICPPTaxesTypeCalc(IKCVTaxesTypeCalc()))

        calc_iss__with_icms = budget.price + iss_with_icms
        calc_icpp_with_ikcv = budget.price + icpp_with_ikcv

        print('calc_iss__with_icms =', str(calc_iss__with_icms))
        print('calc_icpp_with_ikcv =', str(calc_icpp_with_ikcv))

        assert calc_iss__with_icms is not None
        assert calc_icpp_with_ikcv is not None
