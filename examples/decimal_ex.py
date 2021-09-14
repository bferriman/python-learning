# from decimal import Decimal as D

# sum = D(0)
# sum += D("0.01")
# sum += D("0.01")
# sum += D("0.01")
# sum -= D("0.03")
# print("Sum = ", sum)

from decimal import *

sum_1 = Decimal(0)
sum_1 += Decimal("0.0111111111111111")
sum_1 += Decimal("0.0111111111111111")
print("Sum =", sum_1)
sum_1 -= Decimal("0.0222222222222222")
print("Sum =", sum_1)
