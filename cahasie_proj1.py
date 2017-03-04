#Cal Hasie 4/8/12 Project 1


import math

#Lets the user pick if they want to use management or shop mode.
def grocery():
    print("These are the current items, with their quantity and prices at the store:\n")
    in_file = open("grocery_stock.txt","r")            #Shows the user the items in stock from the start of the program
    contents = in_file.readlines()
    print(contents,'\n')
    in_file.close()
    user_pick = int(input("Pick '1' if you want to use MANAGEMENT mode or '2' if you want to use SHOP mode:\n")) 
    if user_pick == 1:                                 #Sends the user to the management function
        manage(contents)
    elif user_pick == 2:                               #Sends the user to the shopping function
        shop(contents)       
    else:
        print("\n!!!You entered a wrong value!!!")


#When user chooses the management option, they will then be asked more quesitons through this function.
def manage(contents):
    products = contents
    in_file = open("grocery_stock.txt","r")
    my_text = open("grocery_stock.txt","a")
    user_man = int(input("\nWhat would you like to manage?\n1- Add new product\n2- Remove a product\n3- Change quantity\n4- Chang price\n5- View table of item info.\n6- Change between manage and shop mode.\n\nEnter what you would like to do here:"))
    if user_man == 1:                                  #Lets the user add the item alond with its quantity and price to the file
        add_item = input("\nEnter the PRODUCT you wish to add:")
        add_quant = int(input("\nEnter the QUANTITY of the product:"))
        add_iprice = float(input("\nEnter the PRICE of the product:"))
        my_text.write(str(add_item)+' '+str(add_quant)+' '+str(add_iprice)+'\n') #Writes the user input text to the file
        my_text.close()
        manage(contents)
    elif user_man == 2:                                #Lets user remove an item from the store file
        rem_item = int(input("\nEnter the row of the item you wish to remove from the list:"))
        del products[rem_item-1]
        print(contents)
        in_file.close()
        manage(contents)
    elif user_man == 3:                                #Allows the change of quantities of items
        item_quant = input("\nWhich item do you wish to change the quantity of?:")
        quant_change = int(input("\nWhat quantity do you wish to change it to?:"))
        manage(contents)
    elif user_man == 4:                                #Allows the change of prices of items
        item_price = input("\nWhich item do you wish to change the price of:?")
        price_change = int(input("\nWhat price do you wish to change it to?:"))
        manage(contents)
    elif user_man == 5:                                #Shows the user the curry table of items in the file
        print("\nThese are the current items, with their quantity and prices at the store:\n")
        in_file = open("grocery_stock.txt","r")
        contents = in_file.read()
        print(contents,'\n')
        manage(contents)
    elif user_man == 6:
        grocery()
    else:
        print("Thanks for your service!")
        
    
#When user chooses the shop option, they will then be asked more quesitons through this function.
def shop(contents):
    products = contents
    in_file = open("grocery_stock.txt","r")
    my_cart = open("grocery_stock.txt","w")
    user_shop = int(input("\nWhich shopping option would you like to choose?\n1- Add an item to the cart\n2- Remove an item from the cart\n3- Check out\n4- View table of item info.\n5- Change between manage and shop mode.\n\nEnter what you would like to do here:"))
    if user_shop == 1:
        add_cart = input("\nWhat item would you like to add to your shopping cart?:")
        quant_cart = int(input("\nHow many of this item would you like to add?:"))
        my_cart.write(str(add_cart)+' '+str(quant_cart)+'\n')
        shop(contents)
    elif user_shop == 2:                               #Lets the user choose which item they wish to remove
        rem_cart = input("\nEnter the row of the item you would like to remove from your shopping cart:")
        del products[rem_cart-1]                       #Del function allows user to delete an item
        print(contents)
        in_file.close()
        shop(contents)
    elif user_shop == 3:
        print('\n',contents,'\n')
        check_out = print("\nTotal cost of shopping is:\n",contents,'\n')
        shop(contents)
    elif user_shop == 4:
        print("\nThese are the current items, with their quantity and prices at the store:\n")
        my_cart = open("grocery_stock.txt","r")        #Shows the user the items in stock from the start of the program
        contents = my_cart.read()
        print(contents,'\n')
        shop(contents)
    elif user_shop == 5:
        grocery()
    else:
        print("Thanks for your service!")
        
        
        
grocery()
