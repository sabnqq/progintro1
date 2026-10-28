

total_seconds = int(input("Počet sekund: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")
