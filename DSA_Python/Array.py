#Using the Native array Module
from array import array

# Initialize an array of signed integers ('i')
val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# --- Modifications ---
val.insert(1, 50)  # Inserts 50 at index 1. Shifts subsequent elements right.
val.append(90)     # Appends 90 to the very end of the array.
val[2] = 200       # Direct mutation: Overwrites the value at index 2 with 200.

# --- Copying Arrays ---
# Creates a duplicate array using a generator expression, matching the source typecode
copyArray = array(val.typecode, (x for x in val))

print("Copied Array initial state:")
for i in copyArray:
    print(i, end=" ")
print("\n")

# --- Deletions & Removals ---
# EDGE CASE: Ensure index exists before popping to avoid IndexError
if len(copyArray) > 3:
    copyArray.pop(3)  # Removes and returns the element at INDEX 3

if len(copyArray) > 0:
    copyArray.pop()   # Removes and returns the absolute LAST element

# EDGE CASE: .remove() raises a ValueError if the value does not exist
value_to_remove = 8
if value_to_remove in copyArray:
    copyArray.remove(value_to_remove)  # Removes the first occurrence of VALUE 8
else:
    print(f"Value {value_to_remove} not found in copyArray.")

# --- Array Traversals & Slicing ---
print("Slicing first 6 elements of val:")
for i in range(0, min(6, len(val))): # min() prevents IndexError if array is short
    print(val[i], end=" ")
print("\n")

print("Traversing val using index range:")
for i in range(0, len(val)):
    print(val[i], end=" ")
print("\n")

print("Traversing val using direct iterator:")
for v in val:
    print(v, end=" ")
print("\n")

# Slicing creates a sub-array containing elements from start_index to stop_index-1
a = val[2:5]   # Elements from index 2 up to 4
b = val[2:-3]  # Elements from index 2 up to the 3rd element from the end

# --- Dynamic User Input Array ---
arr = array('i', [])
try:
    n = int(input("Enter the length of array: "))
    for i in range(0, n):
        # Enforces type safety by ensuring input parses cleanly to an integer
        element = int(input(f"Enter number for index {i}: "))
        arr.append(element)
        
    print("User generated array:")
    for e in arr:
        print(e, end=" ")
    print()
except ValueError:
    print("Invalid input! Please enter integers only.")

#Using the numpy Library
import numpy as np

# Creating a NumPy array from a list
# NumPy automatically infers the data type (e.g., int64 or int32)
np_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# --- Modifications ---
# Note: NumPy arrays have a fixed size upon creation. 
# Functions like insert() or append() return a NEW array rather than mutating in-place.
np_arr = np.insert(np_arr, 1, 50)  # Returns a new array with 50 at index 1
np_arr = np.append(np_arr, 90)     # Returns a new array with 90 appended
np_arr[2] = 200                    # In-place item assignment works (overwrites index 2)

# --- Copying ---
# Explicitly copy to prevent changes in np_copy from affecting np_arr
np_copy = np_arr.copy()

# --- Deletions ---
# np.delete removes elements by INDEX, returning a new array
if len(np_copy) > 3:
    np_copy = np.delete(np_copy, 3)    # Deletes item at index 3

# To remove by VALUE in NumPy, use boolean indexing (filters out the value)
value_to_drop = 8
np_copy = np_copy[np_copy != value_to_drop]

# --- Traversals and Slicing ---
print("NumPy Array Traversal:")
for x in np_arr:
    print(x, end=" ")
print("\n")

# Vectorized operations (A core advantage of NumPy over standard loops)
print("Vectorized operation (Array multiplied by 2):")    
print(np_arr * 2) 

# Multidimensional NumPy Arrays

# ==========================================
# 1. INITIALIZATION & ATTRIBUTES
# ==========================================

# Creating a 2D Array (Matrix: 2 rows, 3 columns)
matrix_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Inspecting crucial structural properties
print("--- Matrix Properties ---")
print(f"Dimensions (Axes): {matrix_2d.ndim}") # Returns 2
print(f"Shape (Rows, Cols): {matrix_2d.shape}") # Returns (2, 3)
print(f"Total Elements: {matrix_2d.size}")     # Returns 6
print(f"Data Type: {matrix_2d.dtype}\n")         # Returns int64 or int32

# Creating a 3D Array (2 blocks, 3 rows, 4 columns)
matrix_3d = np.zeros((2, 3, 4)) # Pre-filled with 0.0 (float64)

# ==========================================
# 2. INDEXING & SLICING (2D)
# ==========================================
# Syntax: matrix[row_index, column_index]
# Syntax: matrix[row_start:row_stop, col_start:col_stop]

print("--- Indexing & Slicing ---")
# Accessing a specific element: Row index 1, Column index 2 (Value: 6)
print(f"Element at [1, 2]: {matrix_2d[1, 2]}")

# Slicing: Extract all rows, but only column index 1
print(f"All values in Column 1: {matrix_2d[:, 1]}")

# Slicing: Extract a sub-matrix (Row 0, Columns 0 and 1)
print(f"Sub-matrix slice:\n{matrix_2d[0:1, 0:2]}\n")


# ==========================================
# 3. RESHAPING & TRANSIPOSITION
# ==========================================
print("--- Shape Modifications ---")

# Reshaping: Changing structure without changing data
# EDGE CASE: Total elements must match perfectly (2*3 = 6 -> 3*2 = 6)
reshaped = matrix_2d.reshape(3, 2)
print(f"Reshaped to 3x2:\n{reshaped}")

# TRICK: Use -1 to let NumPy calculate the dimension automatically
auto_reshaped = matrix_2d.reshape(1, -1) # Flattens into a 1x6 2D row matrix

# Transposing: Flips rows into columns (Swaps axes)
transposed = matrix_2d.T
print(f"Transposed Matrix (3x2):\n{transposed}\n")


# ==========================================
# 4. MATRIX MATH & BROADCASTING
# ==========================================
print("--- Matrix Mathematics ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise operations (Matrices must have identical shapes)
print(f"Element-wise Addition:\n{A + B}")
print(f"Element-wise Multiplication:\n{A * B}")

# Dot Product / Matrix Multiplication (Standard linear algebra)
# Rule: Columns of first matrix must equal Rows of second matrix
dot_product = np.dot(A, B) # Alternatively: A @ B
print(f"Matrix Multiplication (Dot Product):\n{dot_product}")

# Broadcasting EDGE CASE: Operating on mismatched shapes
# NumPy stretches the smaller array across the larger array automatically
scale_vector = np.array([10, 20])
broadcasted_result = A + scale_vector # Adds 10 to col 0, 20 to col 1 across all rows
print(f"Broadcasting Result:\n{broadcasted_result}\n")


# ==========================================
# 5. AXIS-BASED REDUCTIONS
# ==========================================
print("--- Axis Reductions ---")
# axis=0: Performs operation vertically DOWN columns
# axis=1: Performs operation horizontally ACROSS rows

print(f"Sum of each column (Axis 0): {matrix_2d.sum(axis=0)}")
print(f"Max of each row (Axis 1): {matrix_2d.max(axis=1)}")
