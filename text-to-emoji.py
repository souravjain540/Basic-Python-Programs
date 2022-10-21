def main():
    print(convert(input("Enter any text: ")))

def convert(text):
    return text.replace(":(", "🙁").replace(":)", "🙂")

main()