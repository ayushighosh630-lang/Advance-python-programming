import numpy as np

# Create a one-dimensional NumPy array
arr = np.arange(1, 11)

# Display the array
print("Original Array:", arr)

# Display array elements using indexing
print("First Element:", arr[0])
print("Last Element:", arr[-1])

# Perform slicing
print("First Five Elements:", arr[:5])
print("Elements from index 5 to 9:", arr[5:])

# Perform mathematical operations
print("Addition:", arr + 2)
print("Subtraction:", arr - 2)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

# Display sum and mean
print("Sum of Array:", np.sum(arr))
print("Mean of Array:", np.mean(arr))