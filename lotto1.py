import random


def get_number() -> int:
    try:
        number = int(input(f"Enter the number: "))
    except ValueError:
        print("Enter the number not string")
    return number


def get_numbers() -> list:
    result = []
    while len(result) < 6:
        number = get_number()
        if 1 <= number <= 49:
            if number in result:
                print("The number has already been selected")
            else:
                result.append(number)
        else:
            print("The number should be between 1 and 49")
    return result


def print_numbers(numbers: list):
    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers() -> list:
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 49))
    return list(numbers)

def lotto():
    """Main function with our program."""
    user_numbers = get_numbers()
    print("Your numbers:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

    hits = len(set(user_numbers) & set(random_numbers))

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == "__main__":
    lotto()
