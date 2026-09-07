
def knapsack_bottom_up(values, weights, capacity):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(values, weights, capacity):
    n = len(values)

    dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def solve(i, w):

        if i == 0 or w == 0:
            return 0

        if dp[i][w] != -1:
            return dp[i][w]

        if weights[i - 1] <= w:
            include = values[i - 1] + solve(
                i - 1, w - weights[i - 1]
            )
            exclude = solve(i - 1, w)

            dp[i][w] = max(include, exclude)

        else:
            dp[i][w] = solve(i - 1, w)

        return dp[i][w]

    return solve(n, capacity)


print("0/1 Knapsack Problem")
print("--------------------")

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Values:", values)
print("Weights:", weights)
print("Knapsack Capacity:", capacity)

bottom_up_result = knapsack_bottom_up(values, weights, capacity)
top_down_result = knapsack_top_down(values, weights, capacity)

print("\nUsing Bottom-Up Approach:", bottom_up_result)
print("Using Top-Down Approach:", top_down_result)