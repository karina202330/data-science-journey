# numpy_day1_basics.py
"""
NumPy Basics - Day 1
Author: Karina

Topics Covered:
- Creating arrays
- Predefined arrays (zeros, ones, arange, linspace)
- Properties (shape, size, dtype, ndim)
- Indexing and slicing
- Reshaping and flattening
- Random array generation
"""

import numpy as np

# ---------------------------------
# SECTION: Creating Arrays
# ---------------------------------

# 1. From a list
arr = np.array([1, 2, 3])
print(arr)
print(type(arr))  # numpy.ndarray = NumPy's special array type

# 2. 2D array (Matrix)
arr2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr2d)

# ---------------------------------
# SECTION: Predefined Arrays
# ---------------------------------

# a. All zeros
zeros = np.zeros(9)
print(zeros)

# b. All ones
ones = np.ones([2, 3])  # 2 rows, 3 columns
print(ones)

# c. Range using arange
r = np.arange(1, 20)
print(r)

# d. Evenly spaced values using linspace
line = np.linspace(0, 1, 5)
print(line)

# ---------------------------------
# SECTION: Array Properties
# ---------------------------------

a = np.array([[1, 2], [3, 4]])
print("Shape =", a.shape)
print("Size =", a.size)
print("Datatype =", a.dtype)
print("Dimensions =", a.ndim)

# Notes on dtype:
# - all integers → int32 or int64
# - all decimals → float32
# - mix of int, float, string → <U3 or <U5

# ---------------------------------
# SECTION: Indexing and Slicing
# ---------------------------------

# 1D Indexing
a1d = np.array([1, 2, 3, 4, 5])
print(a1d[1])        # Second element
print(a1d[0:5])      # Full slice

# 2D Indexing
b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(b[2, 2])       # Row 3, Col 3
print(b[:, 2])       # All rows, Col 3
print(b[0])          # First row

# ---------------------------------
# SECTION: Reshaping Arrays
# ---------------------------------

# Convert 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped = arr.reshape(3, 3)
print(reshaped)

# ---------------------------------
# SECTION: Flattening Arrays
# ---------------------------------

arr2D = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
flat = arr2D.flatten()
print(flat)

# ---------------------------------
# SECTION: Random Numbers
# ---------------------------------

random_floats = np.random.rand(10)  # 10 random floats between 0 and 1
print(random_floats)
