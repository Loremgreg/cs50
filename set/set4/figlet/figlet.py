from pyfiglet import Figlet
import sys


figlet = Figlet()

# input = input("Input: ", sys.argv[1])

if len(sys.argv) == 0:
    #random font output
    input = input("Input: ")

    figlet.getFonts()


elif len(sys.argv) == 2:
    figlet.setFont(font=sys.argv[2])
    input = input("Input: ")
    print(figlet.renderText(input))
    for arg in sys.argv[1:]:
        if "-f" or "--font" not in sys.argv[1] or arg != setFont:
            sys.exit("...")




    


