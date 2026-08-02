def selectionSort(a):
    n = len(a)

    # OUTER LOOP: Moves the boundary between the sorted and unsorted sections
    # Everything to the left of index 'i' is already sorted
    for i in range(n):
        
        # Assume the first element of the unsorted section is the minimum
        min_idx = i
        
        # =========================================================================
        # 🔍 ARCHITECTURAL NOTE ON THE INNER LOOP RANGE: range(i, n)
        #
        # Why start at 'i'?
        # The elements before index 'i' are already in their final sorted positions. 
        # We only need to scan the remaining unsorted elements starting from index 'i' 
        # to find the next smallest value.
        # =========================================================================
        for j in range(i, n):
            
            # If we find an element smaller than our current minimum...
            if a[min_idx] > a[j]:
                # Update our tracking index to point to this new smallest value
                min_idx = j
                
        # AFTER finding the absolute minimum in the unsorted section:
        # Swap the smallest found element with the element at the boundary index 'i'
        a[i], a[min_idx] = a[min_idx], a[i]

# --- Driver Execution ---
a = [45, 67, 89, 23, 10]
selectionSort(a)
print("Sorted Array:", a)
