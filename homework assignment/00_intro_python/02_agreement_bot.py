book = input("What's your favorite book? ")

bold_italic = "\033[1;3m"
reset = "\033[0m"

print(f"My favorite book is also {bold_italic}{book}{reset}!")