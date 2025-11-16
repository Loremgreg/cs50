# USA: MM/DD/YYYY
# international: YYYY-MM-DD

# Ask user input month-day-year : formatted like 9/8/1636 or September 8, 1636
# if not valid input prompt again
# Output in YYYY-MM-DD format

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# diviser input en 3 avec .split()
def main():
    
    date_user_input = input("Date: ")
    split_user = split(date_user_input)
    dic_month_num = create_dic(split_user)
    print(dic_month_num)

    # print(split_user) # ['4', '5', '1999']
    m, d, y = int(split_user[0]), int(split_user[1]), split_user[2]
    # print(m, d, y) # 4 5 1999
    print(f"{y}-{m:02}-{d:02}") # 1999-04-05



def split(date_user_input):
    split_user_input = date_user_input.split('/')
    split_list = []
    for input in split_user_input:
        split_list.append(input)
    return split_list


def create_dic(date_parts):
    # This creates a dictionary mapping month names to numbers, e.g., {"January": 1, "February": 2, ...}
    dic_month_list = {name: index for index, name in enumerate(month_list, start=1)}
    # Get the month name, which is the first element of the list passed to the function.
    month_name = date_parts[0]
    # Use the extracted month name to look up its corresponding number in the dictionary.
    value_of_month = dic_month_list.get(month_name)
    return value_of_month


main()




# prendre l'annee le mettre a la premiere position
# prendre les month mettre a la 2 eme position
# prendre les jours mettre a la 3 eme position


# Replacing substrings with the <str>.replace(<old>, <new>) method
# list method .index[] -> mettre chaque 3 parties dans 3 nouvelles liste -> re ecrire en format YYYY-MM-DD


# print("Dates: {0}/{1}/{2}. format() )
