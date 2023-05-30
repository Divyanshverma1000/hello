import random
import array as arr

# creating an array with integer type
a= arr.array('i', [1, 2, 3, , , , ,])

# printing original array
print("The new created array is : ", end =" ")
for i in range(0, 2):
	print(a[i], end =" ")
print(random.choice(a))


	

