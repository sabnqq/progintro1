
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return None


def main():
    print(" Celsius | Fahrenheit | Kelvin")
    print("--------------------------------")

    for celsius in range(-40, 101, 20):
        fahrenheit = convert_temperature(celsius, "C", "F")
        kelvin = convert_temperature(celsius, "C", "K")

        print(
            f"{celsius:8.2f} | "
            f"{fahrenheit:10.2f} | "
            f"{kelvin:6.2f}"
        )


if __name__ == "__main__":
    main()
