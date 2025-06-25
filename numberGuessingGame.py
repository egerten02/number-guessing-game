import random

def get_rand_number():
    """Generates a random number."""
    rand_num = random.randint(0, 100)
    return rand_num

def get_guess():
    """Gets a number guess from user."""
    a = input("Make a guess: ")
    try:
        return int(a)
    except ValueError:
        print("Numbers only...")

def compare(guess, number):
    """Compares two number."""
    if guess < number:
        print("Too small.")
    elif guess > number:
        print("Too big")

def main():
    rand_number = get_rand_number()
    guess_count = 0
    total_chance = 8

    while guess_count != total_chance:
        guess_count += 1
        user_guess = get_guess()
        while user_guess is None:
            user_guess = get_guess()

        if user_guess == rand_number:
            print(f"Correct, you guessed it in {guess_count} try.")
            break
        compare(user_guess, rand_number)

        if guess_count == total_chance:
            print(f"You're out of guesses, answer was {rand_number}.")
            break

if __name__ == '__main__':
    main()