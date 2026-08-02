def mergeSort(arr, l, r):
    """
    Recursively divides the array into halves.
    l: left index of the current sub-array
    r: right index of the current sub-array
    """
    # BASE CASE: If l == r, the sub-array has 1 element and is already sorted.
    # The recursion continues only if l < r.
    if l < r:
        # Calculate the middle index to split the array
        # Using integer division (//) to avoid float results
        m = (l + r) // 2

        # DIVIDE PHASE:
        # Recursively sort the left half: from index 'l' to 'm'
        mergeSort(arr, l, m)
        # Recursively sort the right half: from index 'm + 1' to 'r'
        mergeSort(arr, m + 1, r)

        # CONQUER & COMBINE PHASE:
        # Merge the two sorted halves back into the original array
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    """Merges two sorted sub-arrays: arr[l..m] and arr[m+1..r]"""
    # Calculate the sizes of the two temporary sub-arrays
    s1 = m - l + 1  # Size of the left sub-array
    s2 = r - m      # Size of the right sub-array

    # Create temporary placeholder arrays initialized with zeros
    L = [0] * s1
    R = [0] * s2

    # Copy data from the main array into the temporary left array (L)
    for i in range(s1):
        L[i] = arr[l + i]

    # Copy data from the main array into the temporary right array (R)
    for j in range(s2):
        R[j] = arr[m + 1 + j]

    # Initialize starting indices for tracking arrays:
    i = 0  # Initial index of the first sub-array (L)
    j = 0  # Initial index of the second sub-array (R)
    k = l  # Initial index of the merged sub-array back in the main 'arr'

    # Compare elements from L and R, and copy the smaller one back into 'arr'
    while i < s1 and j < s2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1  # Move the main array pointer forward

    # EDGE CASE: If elements remain in L (R finished first), copy them over
    while i < s1:
        arr[k] = L[i]
        i = i + 1
        k = k + 1

    # EDGE CASE: If elements remain in R (L finished first), copy them over
    while j < s2:
        arr[k] = R[j]
        j = j + 1
        k = k + 1

# --- Driver Execution ---
arr = [21, 45, 24, 89, 7, 5, 10]

# Initial call spans from index 0 to the very last index (len - 1)
mergeSort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)
