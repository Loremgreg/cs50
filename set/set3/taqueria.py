taqueria_price = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total_cost= 0

    while True:
        try:
            item = input("Item: ").title()
            value = taqueria_price.get(item)
            if value is not None:
                total_cost += value
                print(f"Total: ${total_cost:.2f}", end="\n")

        except EOFError:
            print()
            break



main()
