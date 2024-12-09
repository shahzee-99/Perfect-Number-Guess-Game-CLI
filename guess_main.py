import random

def update_high_score(attempts):

    try:
        with open("high_score.txt") as f:
            high_score = int(f.read())

        if attempts < high_score:
            with open("high_score.txt", "w") as f:
                f.write(str(attempts))
            print("New high score!")

    except FileNotFoundError:
        print("High score file not found. Creating one...")
        with open("high_score.txt", "w") as f:
            f.write(str(attempts))

def main():
    starting_point = int(input("Enter the number where you want to start the guessing range: "))
    ending_point = int(input("Enter the number where you want to end the guessing range: "))
    number = random.randint(starting_point, ending_point)
    
    while True:
        attempts = 1

        while True:
            print("\n=========================================================\n")
            try:
                user_guess = int(input(f"Enter your guess ({starting_point}-{ending_point}): "))
                if user_guess < starting_point or user_guess > ending_point:
                    print(f"Please guess within the range {starting_point} to {ending_point}.")
                    continue

            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if user_guess == number:
                print(f"Congrats! You guessed the number in {attempts} attempts.")
                update_high_score(attempts)
                break

            elif user_guess > number:
                print("Too high! Try a lower number.")

            else:
                print("Too low! Try a higher number.")
            attempts += 1

        choice = input("Do you want to play again (yes/no)? ").strip()
        if choice in ["yes", "y", "YES"]:
            number = random.randint(starting_point, ending_point)

        elif choice in ["no", "n", "NO"]:
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice! Please enter yes or no.")

if __name__ == "__main__":
    main()
