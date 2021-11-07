from random import *


class StockExchange:
    def __init__(self):
        self.value_actual = 1

        self.value_min = 0.5
        self.value_max = 2

        self.coeff_min = 5
        self.coeff_max = 15

    def get_stock_exchange_prize(self):
        return float("{:.2f}".format(self.value_actual))

    def update_coefficient(self):
        self.value_actual *= randint(self.coeff_min, self.coeff_max)/10
        if self.value_actual <= self.value_min:
            self.value_actual = self.value_min
        elif self.value_actual >= self.value_max:
            self.value_actual = self.value_max
        print(self.value_actual)

    def sale_code(self, stock_code):
        benefit = stock_code * self.value_actual
        return benefit