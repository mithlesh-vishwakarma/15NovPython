# ============================================
# NUMPY BASICS NOTES
# ============================================


# ============================================
# 1. IMPORT NUMPY
# ============================================

import numpy as np  # importing numpy with alias 'np'

# ============================================
# 2. CREATE NUMPY ARRAY
# ============================================

k = np.array([[10, 20, 30], [40, 50, 60]])

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
