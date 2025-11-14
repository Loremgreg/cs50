
def main():
    grocery_list = {}

    while True:
        try:
            item = input("").upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1


        except EOFError:
            for i in sorted(grocery_list.keys()):
                print(grocery_list[item])

            break


# def alphabetic_order(counts):
#     sorted_count = sorted(counts)
#     return sorted_count


main()
