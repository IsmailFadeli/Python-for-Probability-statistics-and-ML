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