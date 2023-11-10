def squared_sum(num):
    return sum(int(digit) ** 2 for digit in str(num))

def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = squared_sum(num)
    return num == 1

num = int(input("Masukkan Angka : "))
if is_happy_number(num):
    print(num, "Adalah Happy Number / true")
else:
    print(num, "Bukan Happy Number / false")
