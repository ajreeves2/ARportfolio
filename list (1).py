#Anyla Reeves
#1/27/25
#Period:5
# create a list

# init
shoppingList = ["Shampoo", "Brush", "Candy", "Toothpaste"] # empty

#function

#main
def shopping_list():
    global shoppingList
    print("Welcome to shopping list organizer")
    print("Try adding a few things to start:")

    while True:

        print("1. view shopping list\n2. add things \n3. remove item \n4. quit")
        #collecting Input
        try:
            ans = input("Type a number betweeen 1 and 4:")
            ans = int(ans)
        except:
            print("ERROR: 4")

        # process the information
        if ans == 1:
            print("Here is your movir watch list")
            print(shoppingList)
        if ans == 2:
            addItem = input("What item do you want to add to your list?: ")
            shoppingList. append(addItem)
            print("Sucessfuly added " + addItem)

        if ans == 3:
            removeItem = input ("What item do you want to remove from your list?: ")
            shoppingList.remove(removeItem)
            print("You have removed " + removeItem)
        if ans == 4:
            print(shoppingList)
            print("Thank you for using our app ")
            break
#main
shopping_list()
