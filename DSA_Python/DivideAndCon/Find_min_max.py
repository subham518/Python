# Finding Minimum and Maximum using Divide and Conquer
def find_min_max(arr, start, end):
    """
    Recursively splits the array to find min and max values simultaneously.
    start: Left index boundary of the current sub-array
    end: Right index boundary of the current sub-array
    """
    # =========================================================================
    # 🧩 BASE CASE 1: Sub-array has exactly ONE element (start == end)
    # Both min and max point to this single element.
    # Note: Using arr[start] for both returns is cleaner than arr[start], arr[end]
    # =========================================================================
    if start == end:
        return arr[start], arr[start]
    
    # =========================================================================
    # 🧩 BASE CASE 2: Sub-array has exactly TWO elements (start + 1 == end)
    # Compare them directly: 1 comparison determines both min and max for this pair.
    # =========================================================================
    if start + 1 == end:
        if arr[start] < arr[end]:
            return arr[start], arr[end]  # (min, max)
        else:
            return arr[end], arr[start]  # (min, max)
        
    # =========================================================================
    # ➗ DIVIDE PHASE:
    # Find the midpoint to split the array segment into two equal halves
    # =========================================================================
    mid = (start + end) // 2

    # =========================================================================
    # 🔄 CONQUER PHASE (RECURSION):
    # Solve the problem independently for the left and right halves
    # =========================================================================
    min1, max1 = find_min_max(arr, start, mid)       # Left half results
    min2, max2 = find_min_max(arr, mid + 1, end)     # Right half results

    # =========================================================================
    # 🤝 COMBINE PHASE:
    # Merge results by taking the absolute minimum and maximum from both halves
    # =========================================================================
    return min(min1, min2), max(max1, max2)

# --- Driver Execution ---
arr = [23, 14, 45, 3, 6, 10]

# Initial call spans from the first index (0) to the absolute last index (len - 1)
minimum_val, maximum_val = find_min_max(arr, 0, len(arr) - 1)

print("min:", minimum_val)
print("max:", maximum_val)
