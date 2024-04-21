import numpy as np;

l1 = np.zeros(10)
print(l1)

l2 = np.ones(10)
print(l2)

l3 = np.ones(10)+4
print(l3)

l4 = np.arange(10,51)
print(l4)

l5 = np.array(l4[l4%2==0])
print(l5)

l6 = np.arange(0,9).reshape(3,3)
print(l6)

l7 = np.eye(3)
print(l7)

l8 = np.random.randint(1)
print(l8)