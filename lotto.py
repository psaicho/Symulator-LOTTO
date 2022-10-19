import random


def lotto() -> list:
    liczby = set()
    while len(liczby) < 6:
        liczby.add(random.randint(1, 49))
    return sorted(list(sorted(liczby)))


def get_player_number() -> list:
    player_number = []
    dic_of_selected_number = ["first", "second", "trird", "fourth", "fifth", "sixth"]
    while len(player_number) < 6:
        try:
            tmp_number = int(input(f"Enter the {dic_of_selected_number[len(player_number)]} number: "))
        except ValueError:
            print("Enter the number not string")
            continue
        if 1 <= tmp_number <= 49:
            if tmp_number in player_number:
                print("The number has already been selected")
            else:
                player_number.append(tmp_number)
        else:
            print("The number should be between 1 and 49")
    print(f"Selected Numbers: {', '.join(str(i) for i in player_number)}.")
    return sorted(player_number)


def result(first_list: list, second_list: list):
    random_numbers = first_list
    player_choice = second_list
    print(f"Drawn numbers: {', '.join(str(i) for i in random_numbers)}.")
    common_elements = list(set(random_numbers) & set(player_choice))
    print(f"You guessed right {len(common_elements)} number(s)" if len(common_elements) > 0 \
              else "Unfortunately you didn't hit any number, please try again")


if __name__ == "__main__":
    result(lotto(), get_player_number())
