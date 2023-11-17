def count_paths(n, grid):
    # Matriks untuk menyimpan jumlah jalur optimal ke setiap sel
    dp = [[0] * n for _ in range(n)]

    # Inisialisasi dp[0][0] berdasarkan kondisi awal
    dp[0][0] = 1 if grid[0][0] == '.' else 0

    # Mengisi dp untuk setiap sel berdasarkan kondisi grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                dp[i][j] = 0  # Tidak bisa melewati sel dengan jebakan
            else:
                # Menambahkan jumlah jalur dari sel di atas dan sel di kiri
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    # Mengembalikan jumlah jalur optimal ke kotak kanan bawah
    return dp[n - 1][n - 1]

# Membaca input
n = int(input("Input: "))
grid = [input()[:n] for _ in range(n)]  # Memastikan setiap baris memiliki panjang n

# Menghitung dan mencetak output
result = count_paths(n, grid)
print("Output:", result)
