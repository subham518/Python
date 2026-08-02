# Problem:
# You are given an array A of n elements.
# You have to remove exactly n/2 elements from an array and add it to another array B (initially empty).
# Find the maximum and minimum values of difference between these two arrays.
# The difference between those two arrays is sum(abs(A[i]-B[i]).


def Max_min_diff(arr):
    # Sort the array in ascending order.
    # Sorting is the core greedy step that allows us to easily pair optimal elements.
    arr.sort()
    
    n = len(arr)
    mid = n // 2   # Find the boundary split point (exactly half the array size)
    max_sum = 0 
    min_sum = 0
    
    # Pointer 'j' starts at the very end of the sorted array (index -1)
    # This points to the largest remaining elements.
    j = -1 

    # Loop exactly n/2 times to pair up elements for both sub-arrays
    for i in range(mid):
        # =========================================================================
        # 🔥 GREEDY STRATEGY: MAXIMUM DIFFERENCE
        # Pair the smallest available elements (from the front: arr[i]) with the 
        # largest available elements (from the back: arr[j]).
        # This maximizes the distance between each paired coordinate.
        # =========================================================================
        max_sum = max_sum + abs(arr[i] - arr[j])
        j = j - 1  # Move the back pointer inward to the next largest element

        # =========================================================================
        # ❄️ GREEDY STRATEGY: MINIMUM DIFFERENCE
        # Pair adjacent items in the sorted array (arr[2*i] and arr[2*i + 1]).
        # Because the array is sorted, adjacent elements have the smallest possible
        # numerical distance between each other.
        # =========================================================================
        min_sum = min_sum + abs(arr[2 * i] - arr[2 * i + 1])
    
    # Output the cumulative difference scores
    print("Max Difference:", max_sum)
    print("Min Difference:", min_sum)

# --- Driver Execution ---
# Array must contain an even number of elements so it can be split exactly in half
arr = [12, 5, 25, 10, 2, 15, 8, 30]
Max_min_diff(arr)
