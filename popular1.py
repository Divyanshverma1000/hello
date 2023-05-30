import random

A = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(A[1])
for i in A:
    for j in i:
        print(j,end = " ")
        
    print(random.choice(A))
