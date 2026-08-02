def QuickSort(arr, l, r):
    """
    Recursively sorts an array using a divide-and-conquer strategy.
    l: Left bounding index of the sub-array
    r: Right bounding index of the sub-array
    """
    # BASE CASE: Continue splitting only if the sub-array has at least 2 elements
    if l < r:
        # Divide phase: Find the partition index 'p' where the pivot is in its final position
        p = partition(arr, l, r)
        
        # Conquer phase: Recursively sort elements strictly to the left of the pivot
        QuickSort(arr, l, p - 1)
        
        # Conquer phase: Recursively sort elements strictly to the right of the pivot
        QuickSort(arr, p + 1, r)

def partition(arr, l, r):
    """
    Rearranges elements around a pivot. Places the pivot at its correct sorted position 
    and returns its final index.
    """
    # Choose the absolute leftmost element as the pivot point
    pivot = arr[l]
    
    # Initialize pointers: 'i' scans forward from left, 'j' scans backward from right
    i = l + 1
    j = r

    while True:
        # Move pointer 'i' right as long as elements are smaller than or equal to the pivot
        # The condition 'i <= j' prevents the pointer from flying past 'j' out of bounds
        while i <= j and arr[i] <= pivot:
            i += 1

        # Move pointer 'j' left as long as elements are strictly greater than the pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        # If pointers haven't crossed yet, it means we found mismatched elements on both sides:
        # - arr[i] is greater than the pivot (should be on the right side)
        # - arr[j] is smaller than or equal to the pivot (should be on the left side)
        if i < j:
            # Swap them to correct their relative positions
            arr[i], arr[j] = arr[j], arr[i]
        else:
            # Pointers have met or crossed (i >= j), meaning partitioning for this segment is complete
            break

    # Swap the pivot element (located at index 'l') with the element at index 'j'
    # This places the pivot exactly where it belongs in the sorted array layout
    arr[l], arr[j] = arr[j], arr[l]

    # Return the index of the pivot so the parent recursive call knows where to split next
    return j

# --- Driver Execution ---
arr = [23, 45, 12, 65, 34, 10, 3]

# Initial call maps across the full range: from index 0 to the absolute last element
QuickSort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)
