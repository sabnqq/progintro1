
diameters = [
    25.01, 24.97, 25.06, 25.00, 24.94,
    25.03, 25.05, 24.95, 25.10, 24.99
]

nominal = 25.00
tolerance = 0.05
defective = 0

for i, d in enumerate(diameters, start=1):
    if d < nominal - tolerance:
        result = "MALY"
        defective += 1
    elif d > nominal + tolerance:
        result = "VELKY"
        defective += 1
    else:
        result = "OK"

    print(f"{i:2}: {d:.2f} mm  {result}")

percentage = defective / len(diameters) * 100
print(f"Zmetku: {defective} z {len(diameters)} ({percentage:.1f} %)")
