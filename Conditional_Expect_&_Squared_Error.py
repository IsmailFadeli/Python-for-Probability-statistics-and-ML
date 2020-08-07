import sympy as S
from sympy.stats import density, E, Die

x = Die('D1', 6)             # 1st six sided die
y = Die('D2', 6)             # 2nd six sided die
a = S.symbols('a')
z = x+y                      # sum of 1st and 2nd die
J = E((x-a*(x+y))**2)        # expectation
print(S.simplify(J))         # J = 329*a**2/6 - 329*a/6 + 91/6
sol,= S.solve(S.diff(J,a),a) # using calculus to minimize
print(sol) # solution is 1/2

import numpy as np
from sympy import stats
# Eq constrains Z
samples_z7 = lambda : stats.sample(x, S.Eq(z,7))    # calls the x variable subject to a condition on the z variable
# it generates random samples of x die, given that the sum of the outcomes of that die and the y die add up to z==7
# using 6 as an estimate
mn = np.mean([(6-samples_z7())**2 for i in range(100)])
# 7/2 is the MSE estimate
mn0= np.mean([(7/2.-samples_z7())**2 for i in range(100)])
print("MSE = %3.2f using 6 vs MSE = %3.2f using 7/2 ", (mn,mn0))

# here 6 is ten times more  probable than any other outcome
x = stats.FiniteRV('D3', {1:1/15., 2:1/15.,
                          3:1/15., 4:1/15.,
                          5:1/15., 6:2/3.})
E(x, S.Eq(z,7)) # conditional expectation E(x/ z = 7) = 5
# we can generate samples and see if this gives the minimum MSE
samples_z7 = lambda : stats.sample(x, S.Eq(z,7))
# using 6 as an estimate
mn = np.mean([(6-samples_z7())**2 for i in range(100)])
# 5 is the MSE estimate
mn0 = np.mean([(5-samples_z7())**2 for i in range(100)])
print("using 6 as Estimate, MSE = ", mn , ". Using 5 as an estimate, MSE = ", mn0)

# output
# 329*a**2/6 - 329*a/6 + 91/6
# 1/2
# MSE = %3.2f using 6 vs MSE = %3.2f using 7/2  (407/50, 2.95000000000000)
# using 6 as Estimate, MSE =  97/25 . Using 5 as an estimate, MSE =  51/20