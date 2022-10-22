def main():
    x = convert(input("Enter time of the day [in hh:mm 24 hour format] : "))

    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)/60
    return hours + minutes


if __name__ == "__main__":
    main()