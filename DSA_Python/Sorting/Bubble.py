def bubbleSort(a):
    n = len(a)

    # OUTER LOOP: Tracks the number of passes through the array
    # Each complete pass guarantees that the next largest element "bubbles" to its correct final position at the end.
    for i in range(n):
        
        # =========================================================================
        # 🔍 ARCHITECTURAL NOTE ON THE INNER LOOP RANGE: range(0, n - 1 - i)
        #
        # Why 'n - 1'?
        # We compare adjacent pairs: a[j] and a[j+1]. If we let 'j' reach the very 
        # last index (n-1), 'j+1' would equal 'n', causing an 'IndexError' (out of bounds).
        # Therefore, 'j' must stop at 'n - 2' so 'j+1' points safely to 'n - 1'.
        #
        # Why '- i'?
        # Optimization! After 'i' passes, the 'i' largest elements have already settled 
        # at the end of the array in their perfect sorted positions. We do not need to 
        # re-check or compare them anymore. Subtracting 'i' prevents redundant comparisons.
        # =========================================================================
        for j in range(0, n - 1 - i):
            
            # Condition for sorting in ascending order
            # Change '>=' to '<=' if you want to sort in descending order
            if a[j] >= a[j+1]:
                # In-place value swap using Python's tuple unpacking
                a[j], a[j+1] = a[j+1], a[j]

# --- Driver Execution ---
a = [45, 67, 89, 23, 10]
bubbleSort(a)
print("Sorted Array:", a)
