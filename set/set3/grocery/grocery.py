# input user item, case insensit
# until ctrl d
# output list sorted alphabet and all uppercase
# + prefixe item with number of time that item was input
#  keys are items and the values are counts.
def main():
    grocery_list = {}

    while True:
        try:
            item = input().upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1

        except EOFError:
            # Sauter une ligne pour un affichage propre après Ctrl-D
            print()
            # Trier les clés du dictionnaire par ordre alphabétique
            for item in sorted(grocery_list.keys()):
                # Afficher le nombre et l'article en majuscules
                print(grocery_list[item], item)
            break

main()
