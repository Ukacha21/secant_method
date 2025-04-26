# import math
from math import *
# import math
from dataclasses import dataclass

@dataclass
class Secant:
    # x_res = 0 #to be assigned at result

    digits: int = 6

    x_0: int = 5
    x_m1: int = 10
    x_curr: int = 0    
    counter: int = 0 #cunku 1. iterasyondan basliyon, sifirinci degil
    stop_control: bool = False

    result_list = []

    x_prev = x_0
    x_2nd_prev = x_m1

    
#function
    def fx(self, x, *bjnm):
        # def fx(self, x, *bjnm):
        #     if abs(x) < 1e-12:
        #         return float('inf')  # or some big value to prevent division by zero
        #     formula = (pow(e, x)/x) - sin(x)/(pow(x, 2)) + 2*x - 10
        #     return formula

        #formula
        # formula = (pow(e, x)/x) - radians(sin(x))/(pow(x, 2)) + 2*x -10
        formula = (pow(e, x)/x) - sin(x)/(pow(x, 2)) + 2*x -10

        # res = 0
        return formula

    def iterate(self, *args):
        if self.stop_control == False:
            self.counter += 1

            denominator = self.fx(self.x_2nd_prev) - self.fx(self.x_prev)
            #           ((self.fx(self.x_2nd_prev)) - self.fx(self.x_prev)) #yes it's the same
            if abs(denominator) < 1e-12:
                self.stop_control = True
                raise ZeroDivisionError("Zero Division Error")
                # return

            self.x_curr = self.x_prev - ((self.fx(self.x_prev) * (self.x_2nd_prev - self.x_prev)) / denominator)
           
            take_sixth = f"{self.x_curr:.{self.digits}f}"
            self.x_curr = float(take_sixth)
            self.result_list.append(self.x_curr)

            try:
                self.x_prev = self.result_list[-1]
                self.x_2nd_prev = self.result_list[-2]
            except:
                pass
            # x_res = x_curr.
            if self.counter >= 1:
                try:

                    for i in range(1, len(self.result_list)):
                        if self.result_list[i] == self.result_list[i-1]:
                            self.stop_control = True
                except:
                    pass
            self.iterate()
        else:
            mini_count = 0
            #gor result
            for i in self.result_list:
                mini_count += 1
                res = f"iteration: {mini_count}  |    result: {i}"
                print(res)
            print(f"x kok degeri:        {self.result_list[-1]}")
            print(f"counter: {self.counter}")

if __name__ == "__main__":
    Secant().iterate()