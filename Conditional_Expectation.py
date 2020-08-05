from sympy.abc import y,x
from sympy import integrate, simplify
fxy = x + y                     # joint density
fy = integrate(fxy, (x,0,1))    # marginal density
fx = integrate(fxy, (y,0,1))    # marginal density

EXY = ((3*y)+2)/((6*y)+3)   # conditional expectation
#   from the definition
LHS=integrate((x-EXY)**2*fxy,(x,0,1),(y,0,1))
print("LHS is ",LHS) #   left-hand-side

#   using Pythagorean theorem
RHS = integrate((x)**2*fx,(x,0,1))-integrate((EXY)**2*fy,(y,0,1))
print("Rhs is ", RHS) # right-hand-side

print (simplify(LHS-RHS) == 0)
