'''
This module contains a methods to calculate the first 10 Fibonacci numbers and print them.
'''


class Fibonacci:
    ''' A collection of methods to calculate and print the first 10 Fibonacci numbers. '''

    def fibonacci(self):
        '''Calculate the first 10 Fibonacci numbers.'''
        num1, num2 = 0, 1
        fib_list = [0, 1]
        for _ in range(2, 10):
            num3 = num1 + num2
            fib_list.append(num3)
            num1, num2 = num2, num3
        return fib_list

    def print_fibonacci(self):
        '''Print the output of the fibonacci function.'''
        fib_numbers = self.fibonacci()
        print(f"The first 10 Fibonacci numbers are: {fib_numbers}")
