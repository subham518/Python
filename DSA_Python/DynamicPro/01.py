# 0/1 Knapsack Problem using Bottom-Up Dynamic Programming
def knapsackDP(weight, value, capacity):
    n = len(weight)

    # Initialize a 2D DP table with dimensions (n + 1) x (capacity + 1) filled with zeros
    # dp[i][w] represents the max profit using the first 'i' items with a knapsack capacity of 'w'
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Populate the table bottom-up
    # i tracks items (1 to n), w tracks current sub-capacity (1 to capacity)
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            
            # Check if the weight of the current item can fit in the current sub-capacity 'w'
            # Index is 'i - 1' because weight and value lists are 0-indexed
            if weight[i - 1] <= w:
                # OPTION 1: Exclude the item -> Take profit from the previous row at same capacity: dp[i - 1][w]
                # OPTION 2: Include the item -> Add current item value + remaining capacity profit: dp[i - 1][w - weight[i - 1]] + value[i - 1]
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + value[i - 1])
            else:
                # The item is too heavy to fit in sub-capacity 'w'. Forcefully exclude it.
                dp[i][w] = dp[i - 1][w]

    # The absolute bottom-right corner holds the solution for all items at maximum capacity
    print("Max Profit is:", dp[n][capacity])

# --- Driver Execution ---
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsackDP(weights, values, capacity)
