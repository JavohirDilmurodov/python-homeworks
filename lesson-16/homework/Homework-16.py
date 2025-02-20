import numpy as np

#1. 100 NumPy exercises.

print(np.__version__)
np.show_config()
zeros = np.zeros(10)
vec = np.arange(10,50)
print(vec)
print(vec[::-1])

rand_vec = np.random.random((10,10))
print(rand_vec.min(), rand_vec.max())


#2. Create a NumPy array of integers from 1 to 10 (inclusive). 
# Calculate the square of each element in the array.
# Find the sum, mean, and standard deviation of the squared array.

array = np.arange(11)
new_array = np.square(array)

print(f"Sum of the new array: {np.sum(new_array)}")
print(f"Mean of the new array: {np.mean(new_array)}")
print(f"STD of the new array: {np.std(new_array)}")

