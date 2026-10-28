
mm = float(input("Délka [mm]: "))

cm = mm / 10
meters = mm / 1000
inches = mm / 25.4

print(
    f"{mm:.3f} mm = "
    f"{cm:.3f} cm = "
    f"{meters:.3f} m = "
    f"{inches:.3f} in"
)
