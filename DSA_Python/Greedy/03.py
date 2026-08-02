# Problem [Fractional Knapsack]
# We are given n items with {weight, value) of each item and the capacity of knapsack (bori) W.
# We need to put these items in the knapsack such that the final value of items in the knapsack is maximum.
#item:   0  1  2  3  4
#value:  21 24 12 40 30
#weight: 7  4  6  5  6

def Fractional_knapsack(price, items_wt, capacity):
    n = len(items_wt)

    # List comprehension to pair item features into tuples: (Value, Weight, Value-per-Weight Ratio)
    # The third element (price[i]/items_wt[i]) is our "Greedy Choice Property"
    items = [(price[i], items_wt[i], price[i] / items_wt[i]) for i in range(n)]

    # SORTING PHASE: Bubble/Selection sort hybrid style to arrange items in descending order of ratio
    # Items with the highest profit margin are pushed to the front of the list
    for i in range(n):
        for j in range(i + 1, n):
            if items[i][2] < items[j][2]:
                # Swap elements if the subsequent item has a higher value-to-weight ratio
                items[i], items[j] = items[j], items[i]

    profit = 0
    
    # GREEDY ALLOCATION PHASE: Iterate through sorted items and pack them
    for pri, itm_wt, perKgPrice in items:
        # CASE 1: The full item can fit comfortably inside the remaining knapsack capacity
        if capacity >= itm_wt:
            profit = profit + pri          # Accumulate the item's total full value
            capacity = capacity - itm_wt    # Deduct the item's weight from knapsack capacity
        
        # CASE 2: The full item cannot fit. We take a fraction to top off the knapsack
        else:
            # Fill the remaining space with a fractional value of the current item
            profit = profit + perKgPrice * capacity
            capacity = 0  # Knapsack is now entirely full (capacity reached 0)
            break         # Optional optimization: safe to stop early since capacity is exhausted

    print("Total Profit:", profit)

# --- Driver Execution ---
price = [21, 24, 12, 40, 30]
items_wt = [7, 4, 6, 5, 6]
capacity = 20

Fractional_knapsack(price, items_wt, capacity)
