from math import *
from dataclasses import dataclass

@dataclass
class Secant:
    digits: int = 6
    x_0: float = 5
    x_m1: float = 10
    x_curr: float = 0    
    counter: int = 0
    stop_control: bool = False

    result_list = None

    x_prev: float = None
    x_2nd_prev: float = None

    def __post_init__(self):
        self.result_list = []
        self.x_prev = self.x_0
        self.x_2nd_prev = self.x_m1

    @staticmethod
    def fx(x):
        return (pow(e, x) / x) - (sin(x) / (pow(x, 2))) + (2 * x) - 10

    def iterate(self):
        while not self.stop_control:
            self.counter += 1

            fx_prev = self.fx(self.x_prev)
            fx_2nd_prev = self.fx(self.x_2nd_prev)

            self.x_curr = self.x_prev - (fx_prev * (self.x_2nd_prev - self.x_prev)) / (fx_2nd_prev - fx_prev)
            
            # Round to the desired number of digits
            self.x_curr = float(f"{self.x_curr:.{self.digits}f}")

            self.result_list.append(self.x_curr)

            # Update previous values
            if len(self.result_list) > 1:
                self.x_2nd_prev = self.result_list[-2]
            self.x_prev = self.result_list[-1]

            # Check for stopping condition
            if len(self.result_list) > 1:
                if self.result_list[-1] == self.result_list[-2]:
                    self.stop_control = True

        # After stop, print results
        for idx, val in enumerate(self.result_list, start=1):
            print(f"Iteration: {idx} | Result: {val}")

        print(f"\nFinal x value: {self.result_list[-1]}")


if __name__ == "__main__":
    Secant().iterate()
