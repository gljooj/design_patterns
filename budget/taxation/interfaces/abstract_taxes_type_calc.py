import abc


class AbstractTaxesTypeCalc:
    @abc.abstractmethod
    def type_calc(self, BudgetMedium):
        raise NotImplementedError
