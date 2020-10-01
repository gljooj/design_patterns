import abc


class TaxesNextTaxesService(object):
    def __init__(self, next_taxe=None):
        self.__next_taxe = next_taxe

    def calc_next_taxe(self, budget):
        if self.__next_taxe is None:
            return 0
        else:
            return self.__next_taxe.type_calc(budget)

    @abc.abstractmethod
    def type_calc(self, budget):
        pass
