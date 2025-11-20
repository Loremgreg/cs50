from random import randint

def main():

    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
            else:
                random_num = generate_random_num(n)

                conditional(random_num)
                break
        except ValueError:
            continue


def generate_random_num(n):
    random_num = randint(1, n)
    return random_num

def conditional(random_num):
    while True:
            try:
                guessing_num = int(input("Guess: "))
            except ValueError:
                 continue

            if 0 < guessing_num < random_num:
                print("Too small!")
                continue

            elif guessing_num > random_num:
                print("Too large!")
                continue

            elif guessing_num <= 0:
                continue

            else:
                print("Just right!")
                return

main()
