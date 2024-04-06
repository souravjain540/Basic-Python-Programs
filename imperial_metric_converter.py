import sys


def mk(miles):
    return miles * 1.60934


def km(km):
    return km * 0.621371


def fm(feet):
    return feet * 0.3048


def mf(meters):
    return meters * 3.28084

# USAGE:
# MILES TO KILOMETERS - py.exe imperial_metric_converter.py mk 10
# KILOMETERS TO MILES - py.exe imperial_metric_converter.py km 20
# FEET TO METERS - py.exe imperial_metric_converter.py fm 50
# METERS TO FEET - py.exe imperial_metric_converter.py mf 100


def main():
    if len(sys.argv) < 3:
        print("Usage: python imperialmetricconverter.py <conversion> <value>")
        print("Conversions: mk, km, fm, mf")
        sys.exit(1)

    conversion = sys.argv[1]
    value = float(sys.argv[2])

    if conversion == "mk":
        result = mk(value)
        print(f"{value} miles is equal to {result} kilometers")
    elif conversion == "km":
        result = km(value)
        print(f"{value} kilometers is equal to {result} miles")
    elif conversion == "fm":
        result = fm(value)
        print(f"{value} feet is equal to {result} meters")
    elif conversion == "mf":
        result = mf(value)
        print(f"{value} meters is equal to {result} feet")
    else:
        print("Invalid conversion specified")


if __name__ == "__main__":
    main()
