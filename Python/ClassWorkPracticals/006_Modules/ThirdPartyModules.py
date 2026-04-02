# ============================================
# NUMPY BASICS NOTES
# ============================================


# ============================================
# 1. IMPORT NUMPY
# ============================================

<<<<<<< HEAD
import numpy as np  # importing numpy with alias 'np'

# ============================================
# 2. CREATE NUMPY ARRAY
=======
import numpy as np   # np is alias (short name)


"""
Explanation:

NumPy → Library used for numerical operations

np → Standard alias used for numpy
"""


# ============================================
# 2. CREATING NUMPY ARRAY
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36
# ============================================

k = np.array([[10, 20, 30], [40, 50, 60]])

<<<<<<< HEAD
print(k)  # Output:
# [[10 20 30]
#  [40 50 60]]


# ============================================
# 3. CHECK DIMENSIONS
# ============================================

print(k.ndim)  # Output: 2


# ndim → number of dimensions
# 1D → single list
# 2D → list of lists (matrix)
# 3D → list of matrices


# ============================================
# 4. CHECK SHAPE
# ============================================

print(k.shape)  # Output: (2, 3)


# shape → (rows, columns)

# Here:
# 2 → number of rows
# 3 → number of columns


# ============================================
# UNDERSTANDING THE ARRAY
# ============================================

# k =
# [
#   [10, 20, 30],   ← Row 1
#   [40, 50, 60]    ← Row 2
# ]

# So:
# Rows = 2
# Columns = 3
# Dimensions = 2


# ============================================
# KEY POINTS
# ============================================

# • NumPy array is faster than Python list
# • Used for numerical computations
# • Supports multi-dimensional data
# • Important for data analysis & machine learning
=======
print(k)


"""
Explanation:

np.array() → Creates array

Here:
2D array (matrix)

[
 [10,20,30],
 [40,50,60]
]
"""


# ============================================
# 3. DIMENSIONS OF ARRAY
# ============================================

print(k.ndim)


"""
Explanation:

ndim → Number of dimensions

1D array → ndim = 1
2D array → ndim = 2
3D array → ndim = 3
"""


# ============================================
# 4. SHAPE OF ARRAY
# ============================================

print(k.shape)


"""
Explanation:

shape → (rows, columns)

Here:
(2, 3) → 2 rows and 3 columns
"""


# ============================================
# EXTRA IMPORTANT NOTES
# ============================================

# NumPy array vs Python list:

# • Faster than list
# • Uses less memory
# • Supports vector operations

# Example:
# list → [1,2,3]
# array → np.array([1,2,3])
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36
