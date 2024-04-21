import numpy as np;


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l3 = np.array([(123),(456)])

print(l3)

l4 = np.array(l1) * np.array(l2)
print(l4)

print(np.random.rand(10))
print(np.random.randint(1,100))

print(np.sum(l3))

a = np.arange(5)
b = np.random.randint(1,16, size=(3,5))

print(b)

l5 = np.arange(20)
print(l5)

print(l5[l5%2==0])

l6 = np.arange(2,22,2)
print(l6)