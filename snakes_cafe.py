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
footer = [strs, "** What would you like to order? **", strs, ">"]

Appetizers = ["Wings", "Cookies", "Spring Rolls"]
Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream", "Cake", "Pie"]
Drinks = ["Coffee", "Tea", "Unicorn Tears"]

def hf(section):
    for i in section:
        print(i)
    print("")

def menu_items(list):
    lnames = [name for name in globals() if globals()[name] is list]
    print(lnames)
    print("----------")
    for x in list:
        print(x)
    print("")


hf(header)
menu_items(Appetizers)
menu_items(Entrees)
menu_items(Desserts)
menu_items(Drinks)
hf(footer)
