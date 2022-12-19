# In the name of GOD
# MmSh
# Generating N random numbers 

import math
import random

N = int(input(" Enter your N for number of Generate Random : "))
# Inverse of Continuous distribution function
# RCDF = math.pow((3/5)*u,1/3)

GRCDF=[]

# Seed
random.seed(123)

for i in range(N):
    Rnd = random.random()
    x = math.pow((3/5)*Rnd,1/3)
    GRCDF.append(x)

print(GRCDF)
    
    


