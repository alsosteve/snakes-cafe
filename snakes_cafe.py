stars = "**************************************"
strs = "***********************************"
header = [
    "$ python snakes_cafe.py",
    stars,
    "**    Welcome to the Snakes Cafe!   **",
    "**    Please see our menu below.    **",
    "**",
    '** To quit at any time, type "quit" **',
    stars
]
footer = [strs, "** What would you like to order? **", strs]

Appetizers = {"Wings": 0, "Cookies": 0, "Spring Rolls": 0}
Entrees = {"Salmon": 0, "Steak": 0, "Meat Tornado": 0, "A Literal Garden": 0}
Desserts = {"Ice Cream": 0, "Cake": 0, "Pie": 0}
Drinks = {"Coffee": 0, "Tea": 0, "Unicorn Tears": 0}

menu = [Appetizers, Entrees, Desserts, Drinks]

def hf(section):
    print("")
    for i in section:
        print(i)

def menu_items(dictionary):
    print("")
    lnames = [name for name in globals() if globals()[name] is dictionary]
    print(lnames[0])
    print("----------")
    for i in dictionary.keys():
        print(i)

def menu_gen(list):
    for i in list:
        menu_items(i)

def item_search(list, inp):
    while True:
        if inp == "quit":
            break
        for i in list:
            if(inp in i):
                i[inp] = i.get(inp) + 1
                print(str(i.get(inp)) + " orders of " + inp + " have been added to your meal")
                user_input(menu)
        break


def user_input(menu):
    order = input("> ")
    item_search(menu, order)



hf(header)
menu_gen(menu)
hf(footer)
user_input(menu)