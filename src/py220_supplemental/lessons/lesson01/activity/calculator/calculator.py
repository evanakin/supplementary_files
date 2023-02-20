""" This module provides a calculator. """


from .exceptions import InsufficientOperands


# pylint: disable=R0205
class Calculator(object):
    '''
    class doc
    '''
    def __init__(self, adder, subtracter, multiplier, divider):
        '''
        function doc
        '''
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        function doc
        """
        self.stack.append(number)

    def _do_calc(self, operator):
        '''
                function doc
                '''
        try:
            result = operator.calc(self.stack[0], self.stack[1])
        except IndexError as exc:
            raise InsufficientOperands from exc

        self.stack = [result]
        return result

    def add(self):
        '''
                function doc
                '''
        return self._do_calc(self.adder)

    def subtract(self):
        '''
                function doc
                '''
        return self._do_calc(self.subtracter)

    def multiply(self):
        '''
                function doc
                '''
        return self._do_calc(self.multiplier)

    def divide(self):
        '''
                function doc
                '''
        return self._do_calc(self.divider)
