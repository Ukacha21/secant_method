# import math
from math import *
from dataclasses import dataclass

# x_res = 0 #to be assigned at result

# digits = 6

# x_0 = 5
# x_m1 = 10

# x_curr = 0
# x_prev = x_0
# x_2nd_prev = x_m1
# counter = 0

# result_list = []

# stop_control = False

@dataclass
class Secant:
    # x_res = 0 #to be assigned at result

    digits: int = 6

    x_0: int = 5
    x_m1: int = 10
    x_curr: int = 0    
    counter: int = 0
    stop_control: bool = False

    result_list = []

    x_prev = x_0
    x_2nd_prev = x_m1

    
#function
    def fx(x):

        #formula
        formula = (pow(e, x)/x) - sin(x)/(pow(x, 2)) + 2*x -10

        # res = 0
        return formula

    def iterate(self):
        if self.stop_control == False:
            self.counter += 1

            self.x_curr = self.x_prev - (self.fx(self.x_prev)*(self.x_2nd_prev - self.x_prev))/((self.fx(self.x_2nd_prev)) - self.fx(self.x_prev))
            self.x_curr = str(self.x_curr)
            # x_curr = x_curr[:7]
            # temp_digit_control = int(x_curr[5]) # 6. basamak 5 oluyor, starting from zero
            # if temp_digit_control >= 5:
            #     temp_digit_control += 1
            #     x_curr = x_curr[:4] + str(temp_digit_control)

            take_sixth = f"{self.x_curr:.6f}"
            self.x_curr = float(take_sixth)
            self.result_list.append(self.x_curr)
            # x_res = x_curr
            if self.counter > 1:
                try:

                    for i in self.result_list:
                        if self.result_list[i] == self.result_list[i-1]:
                            stop_control = True

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
            print(f"x degeri{self.result_list[-1]}")







# #function
# def fx(x):

#     #formula
#     formula = (pow(e, x)/x) - sin(x)/(pow(x, 2)) + 2*x -10

#     # res = 0
#     return formula

# def iterate():
#     if stop_control == False:
#         counter += 1

#         x_curr = x_prev - (fx(x_prev)*(x_2nd_prev - x_prev))/((fx(x_2nd_prev)) - fx(x_prev))
#         x_curr = str(x_curr)
#         # x_curr = x_curr[:7]
#         # temp_digit_control = int(x_curr[5]) # 6. basamak 5 oluyor, starting from zero
#         # if temp_digit_control >= 5:
#         #     temp_digit_control += 1
#         #     x_curr = x_curr[:4] + str(temp_digit_control)

#         take_sixth = f"{x_curr:.6f}"
#         x_curr = float(take_sixth)
#         result_list.append(x_curr)
#         # x_res = x_curr
#         if counter > 1:
#             try:

#                 for i in result_list:
#                     if result_list[i] == result_list[i-1]:
#                         stop_control = True

#             except:
#                 pass
#         iterate()
#     else:
#         mini_count = 0
#         #gor result
#         for i in result_list:
#             mini_count += 1
#             res = f"iteration: {mini_count}  |    result: {i}"
#             print(res)
#         print(f"x degeri{result_list[-1]}")




    # number = 12.34643445
    # formatted = f"{number:.4f}"

# iterate()
        