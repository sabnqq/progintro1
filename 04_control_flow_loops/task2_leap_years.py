
year = int(input("Zadej rok: "))

is_leap = (
    (year % 4 == 0 and year % 100 != 0)
    or year % 400 == 0
)

if is_leap:
    print("Prestupny rok")
else:
    print("Neni prestupny rok")

count = 0

for y in range(1890, 2031):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print(y, end=" ")
        count += 1

        if count % 10 == 0:
            print()

print()
print("Pocet prestupnych roku:", count)
