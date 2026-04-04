# ============================================
# NUMPY BASICS NOTES
# ============================================


# ============================================
# 1. IMPORT NUMPY
# ============================================

import numpy as np  # np is alias (short name)

"""
Explanation:

NumPy → Library used for numerical operations

np → Standard alias used for numpy
"""


# ============================================
# 2. CREATING NUMPY ARRAY
# ============================================

k = np.array([[10, 20, 30], [40, 50, 60]])

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
