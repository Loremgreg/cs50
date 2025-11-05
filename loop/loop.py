# for i in range(3):
#     print("meow")

# print("meow" * 3)


# print("meow\n" * 3, end="")


# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


# def main():
#     meow(get_number())

# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()


# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])


# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student, students[student], sep=", ")


# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")



def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()