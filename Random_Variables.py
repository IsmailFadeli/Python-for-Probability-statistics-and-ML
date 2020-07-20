#   What is the probability that the sum of the dice equals seven?

#   Step 1: associate all of the (a,b) pairs with their sum.

d = {(i,j):i+j for i in range(1,7) for j in range(1,7)}

#   Step 2: collect all of the (a,b) pairs that sum each of the possible values from two to twelve.

from collections import defaultdict
dinv = defaultdict(list)    #  The defaultdict() object creates dictionaries with default values when it encounters a new key.
for i,j in d.items():
    dinv[j].append(i)

print(dinv[7])  #   dinv[7] contains the list of pairs that sum to seven

# Step 3: Compute the probability measured for each of these items.

X = {i:len(j)/36. for i,j in dinv.items() }
print(X)

# What is the probability that half the product of three dice will exceed their sum?
f = {(i,j,k):((i*j*k)/2>i+j+k) for i in range(1,7)
                                    for j in range(1,7)
                                        for k in range(1,7)}

finv = defaultdict(list)
for i,j in f.items(): finv[j].append(i)

Y = {i:len(j)/6.0**3 for i,j in finv.items()}

print(Y)
