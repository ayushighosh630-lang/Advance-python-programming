


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    result = []

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    result.reverse()

    return ''.join(result)


print("Longest Common Subsequence")
print("--------------------------")

X = input("Enter the first sequence: ")
Y = input("Enter the second sequence: ")

answer = lcs(X, Y)

print("Longest Common Subsequence:", answer)
print("Length of LCS:", len(answer))