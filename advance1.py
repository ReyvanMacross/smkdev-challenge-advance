def count_paths(n, grid):
    dp = [[0] * n for _ in range(n)]

    dp[0][0] = 1 if grid[0][0] == '.' else 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                dp[i][j] = 0  
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

 
    return dp[n - 1][n - 1]

n = int(input("Input: "))
grid = [input()[:n] for _ in range(n)]  

result = count_paths(n, grid)
print("Output:", result)
