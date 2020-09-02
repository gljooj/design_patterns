import abc


# calculadora padrão

class AbstractCalculatorMedium:
    @abc.abstractmethod
    def do_calc(self, calc):
        raise NotImplementedError
