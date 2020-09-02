import abc


class AbstractDiscountTypeCalc:
    @abc.abstractmethod
    def type_calc(self, budget):
        raise NotImplementedError
