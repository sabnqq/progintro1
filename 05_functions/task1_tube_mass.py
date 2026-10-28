
import math


def circle_area(d):
    radius = d / 2
    return math.pi * radius ** 2


def tube_cross_section(d_out, d_in):
    outer_area = circle_area(d_out)
    inner_area = circle_area(d_in)
    return outer_area - inner_area


def tube_mass(d_out, d_in, length, density=7850):
    cross_section = tube_cross_section(d_out, d_in)
    volume = cross_section * length
    return volume * density


def main():
    steel_mass = tube_mass(0.060, 0.050, 6)
    aluminum_mass = tube_mass(0.060, 0.050, 6, density=2700)

    print(f"Steel pipe: {steel_mass:.2f} kg")
    print(f"Aluminum pipe: {aluminum_mass:.2f} kg")


if __name__ == "__main__":
    main()
