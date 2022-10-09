import numpy as np

# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# Example
# Create a 0-D array with value 42
arr = np.array(42)
print(arr, '\n')

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.
# Create a 1-D array containing the values 1,2,3,4,5:
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1, '\n')

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2, '\n')

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3, '\n')

# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how
# many dimensions the array have.
# Check how many dimensions the arrays have:
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.
# Create an array with 5 dimensions and verify that it has 5 dimensions:
arr4 = np.array([1, 2, 3, 4], ndmin=5)
print(arr4)
print('number of dimensions :', arr4.ndim)