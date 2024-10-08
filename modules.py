import random


def main():
    try:
        # Main code
        random_value = random.randint(1, 100)  # originally line 4
        user_input = int(input("Enter a number to guess the number: "))
        # Check if the random value is different than the user_input,
        # if so it will run the while code
        while random_value != user_input:
            # Check if the difference is less or equal to 5
            if abs(random_value - user_input) <= 5:
                print("Very hot")
                # Ask the user for the number again
                user_input = int(input("Enter a number to guess the number: "))
            elif (
                abs(random_value - user_input) > 5
                and abs(random_value - user_input) <= 15
            ):
                print("hot")
                user_input = int(input("Enter a number to guess the number: "))
            elif (
                abs(random_value - user_input) > 15
                and abs(random_value - user_input) <= 25
            ):
                print("warm")
                user_input = int(input("Enter a number to guess the number: "))
            else:
                print("cold")
                user_input = int(input("Enter a number to guess the number: "))
    except ValueError:
        print("Is not a valid number")


if __name__ == "__main__":
    main()
