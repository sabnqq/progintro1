
N = 5
total = 0

print(f"Enter {N} numbers:")

for i in range(1, N + 1):
    number = float(input(f"Value #{i}: "))
    total += number

average = total / N
print("Average value:", average)
