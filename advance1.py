def calculate_spiral_value(row, col):
    max_val = max(row, col)
    if max_val % 2 == 0:
        if max_val == row:
            return max_val ** 2 - col + 1
        else:
            return (max_val - 1) ** 2 + row
    else:
        if max_val == col:
            return max_val ** 2 - row + 1
        else:
            return (max_val - 1) ** 2 + col

# Fungsi untuk membaca input dan menghasilkan output
def process_input():
    T = int(input("Masukkan jumlah test case (T): "))
    for _ in range(T):
        row, col = map(int, input("Masukkan baris dan kolom: ").split())
        result = calculate_spiral_value(row, col)
        print(result)

# Memanggil fungsi untuk memproses input
process_input()
