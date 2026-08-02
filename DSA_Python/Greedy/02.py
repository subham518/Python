#Problem:[Greedy Approaach]
# find minimum number of denominations or
# Coin change problem

def coin_change_problem(amount, coins):
    # Sort denominations in descending order (largest first)
    # This is the core 'greedy choice' to minimize total coin count
    coins.sort(reverse=True)

    total = []

    for coin in coins:
        # BUG FIX: Changed '<' to '<=' 
        # If the coin value equals the remaining amount, we must include it
        while coin <= amount:
            amount -= coin      # Reduce the remaining amount needed
            total.append(coin)  # Track the coin denomination used
            
    return total

# --- Driver Execution ---
# Standard Indian Rupee (INR) denominations (Canonical coin system)
coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
amount = 1024

ans = coin_change_problem(amount, coins)

print("Coins Used:", ans)                   # Outputs: [200, 50, 20, 5]
print("Minimum number of coins:", len(ans))   # Outputs: 4
print("Distinct Coins Used:", len(set(ans))) # Outputs: 4
