import numpy as np
x,y = np.random.rand(2,1000)    # uniform rv
a,b,c = x, (y-x), 1-y   # 3 slides
s = (a+b+c)/2
n = np.mean((s>a) & (s>b) & (s>c) & (y>x))  # approx 1/8=0.125
n   # 0.112
