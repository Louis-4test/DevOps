# Simple Python Script

def main():
    # Ask for user's name
    name = input("What's your name? ")

    # Ask for user's age and convert it to an integer
    age = int(input("How old are you? "))

    # Calculate the year the user will turn 100
    current_year = 2024
    year_100 = current_year + (100 - age)

    # Print a message with the result
    print(f"Hello, {name}! You will turn 100 years old in the year {year_100}.")

if __name__ == "__main__":
    main()
