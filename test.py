def restaurant(inventory_file,breakfast,lunch,dinner,orders,sales,feedback_file):
    
    print('Welcome to Hassan Cafe!'.center(30))
    print('*'*30 + '\n')

    select = ''
    while select != '0':

        select = input('Press 1 for inventory\nPress 2 for Menu\nPress 3 for POS\nPress 4 for Feedback\nPress 5 for Sales History\nPress 6 to View Stats\nPress 0 to exit program\n')

        if select == '1':
            inventory(inventory_file)
        elif select == '2':
            menu(breakfast,lunch,dinner)
        elif select == '3':
            pos(orders,breakfast,lunch,dinner,sales)
        elif select == '4':
            feedback(feedback_file)
        elif select == '5':
            history(sales)
        elif select == '6':
            stats(breakfast,lunch,dinner)
        elif select == '0':
            break
        else:
            print('Please select from the menu.')

def inventory(filename):
    
    print('Inventory Menu'.center(70))
    print('*'*70 + '\n')

    def view(filename):
        infile = open(filename)
        inventory = eval(infile.read())
        infile.close()
        for item,quantity in inventory.items():
            print('{:50}{}'.format(item.title(),quantity))
        print()
        
    def increment(filename):
        
        select = 'y'
        while select == 'y':

            try:
                item = input('\nEnter the item: ').casefold()
                quantity = int(input('Enter the quantity to be added: '))
                
                infile = open(filename)
                inventory = eval(infile.read())
                infile.close()

                inventory[item] += quantity

                outfile = open(filename,'w')
                outfile.write(str(inventory))
                outfile.close()

                print('\nInventory item updated!\n')
                select = input('Press y to increment another item.\nPress anything else to go back.\n').casefold()

            except:
                print('\nError! Please enter the correct item name.\n')

    def update(filename):
        
        select = 'y'
        while select == 'y':

            item = input('\nEnter the item: ').casefold()
            quantity = int(input('Enter the new quantity: '))
            
            infile = open(filename)
            inventory = eval(infile.read())
            infile.close()

            inventory[item] = quantity

            outfile = open(filename,'w')
            outfile.write(str(inventory))
            outfile.close()

            print('\nInventory item updated!\n')
            select = input('Press y to update another item.\nPress anything else to go back.\n').casefold()

    def remove(filename):

        select = 'y'
        while select == 'y':

            try:
                item = input('\nEnter the item to be removed: ').casefold()
                
                infile = open(filename)
                inventory = eval(infile.read())
                infile.close()

                del inventory[item]

                outfile = open(filename,'w')
                outfile.write(str(inventory))
                outfile.close()

                print('\nInventory item removed!\n')
                select = input('Press y to remove another item.\nPress anything else to go back.\n').casefold()

            except:
                print('\nError! Please enter the correct item name.\n')

    select = ''
    while select != '0':

        select = input('Press 1 to view inventory\nPress 2 to increase/decrease inventory items\nPress 3 to add new items and/or update quantity of items\nPress 4 to delete an item from inventory\nPress 0 to go back to main menu\n')

        if select == '1':
            view(filename)
        elif select == '2':
            increment(filename)
        elif select == '3':
            update(filename)
        elif select == '4':
            remove(filename)
        elif select == '0':
            pass
        else:
            print('\nPlease select from the menu.\n')

def menu(breakfast,lunch,dinner):
    
    print('Menu'.center(70))
    print('*'*70 + '\n')

    def view(breakfast,lunch,dinner):

        def viewer(file):
            infile = open(file)
            menu = eval(infile.read())
            infile.close()
            print('{:56}{:12}{:}'.format('\nDish','Available','Price\n'))
            for dish,quantityCost in menu.items():
                print('{:40}{:20}{:10}'.format(dish.title(),quantityCost[0],quantityCost[1]))
            print()


        select = ''
        while select != '0':

            select = input('Press 1 for Breakfast\nPress 2 for Lunch\nPress 3 for Dinner\nPress 0 to go back\n')

            if select == '1':
                print('Breakfast Menu'.center(70))
                print('^'*70)
                viewer(breakfast)

            elif select == '2':
                print('Lunch Menu'.center(70))
                print('^'*70 + '\n')
                viewer(lunch)

            elif select == '3':
                print('Dinner Menu'.center(70))
                print('^'*70 + '\n')
                viewer(dinner)

            elif select == '0':
                pass

            else:
                print('Please select from the menu.\n')

    def update(breakfast,lunch,dinner):

        def updater(file):

            infile = open(file)
            menu = eval(infile.read())
            infile.close()

            select = 'y'
            while select == 'y':

                try:
                    dish = input('Enter the name of the dish: ').casefold()
                    cost = int(input('Enter the cost of this dish: '))
                    servings = int(input('Enter how many servings available per day: '))
                    menu[dish] = [servings,cost,0]

                    print('\nDish updated!\n')
                    select = input('Press Y to add or update another dish. Press anything else to go back.\n').casefold()

                except ValueError:
                    print('\nError! Please enter a number for cost and/or servings\n')
                except:
                    print('\nError!\n')

            outfile = open(file,'w')
            outfile.write(str(menu))
            outfile.close()

        select = ''
        while select != '0':

            select = input('Press 1 for Breakfast\nPress 2 for Lunch\nPress 3 for Dinner\nPress 0 to go back\n')

            if select == '1':
                updater(breakfast)
                
            elif select == '2':
                updater(lunch)

            elif select == '3':
                updater(dinner)

            elif select == '0':
                pass

            else:
                print('Please select from the menu.\n')

    def remove(breakfast,lunch,dinner):

        def remover(file):

            infile = open(file)
            menu = eval(infile.read())
            infile.close()

            select = 'y'
            while select == 'y':

                try:
                    dish = input('Enter the name of the dish: ').casefold()
                    del menu[dish]
                    print('\nDish removed from menu.\n')
                    select = input('Press Y to add or update another dish. Press anything else to go back.\n').casefold()

                except:
                    print('\nError! Please enter the correct item name.\n')

            outfile = open(file,'w')
            outfile.write(str(menu))
            outfile.close()

        select = ''
        while select != '0':

            select = input('Press 1 for Breakfast\nPress 2 for Lunch\nPress 3 for Dinner\nPress 0 to go back\n')

            if select == '1':
                remover(breakfast)

            elif select == '2':
                remover(lunch)

            elif select == '3':
                remover(dinner)

            elif select == '0':
                pass

            else:
                print('Please select from the menu.\n')

    def servings(breakfast,lunch,dinner):
        
        def servingsChanger(file):

            infile = open(file)
            menu = eval(infile.read())
            infile.close()

            select = 'y'
            while select == 'y':

                try:
                    dish = input('Enter the name of the dish: ').casefold()
                    servings = int(input('Enter how many servings available per day: '))
                    menu[dish][0] = servings
                    print('\nServings updated!\n')
                    select = input('Press Y to update servings of another dish. Press anything else to go back.\n').casefold()

                except ValueError:
                    print('\nError! Please enter a valid number for servings\n')
                except KeyError:
                    print('\nError! Please enter the correct dish name.\n')

            outfile = open(file,'w')
            outfile.write(str(menu))
            outfile.close()

        select = ''
        while select != '0':

            select = input('Press 1 for Breakfast\nPress 2 for Lunch\nPress 3 for Dinner\nPress 0 to go back\n')

            if select == '1':
                servingsChanger(breakfast)
                
            elif select == '2':
                servingsChanger(lunch)

            elif select == '3':
                servingsChanger(dinner)

            elif select == '0':
                pass

            else:
                print('Please select from the menu.\n')

    def cost(breakfast,lunch,dinner):

        def costChanger(file):

            infile = open(file)
            menu = eval(infile.read())
            infile.close()

            select = 'y'
            while select == 'y':

                try:
                    dish = input('Enter the name of the dish: ').casefold()
                    cost = int(input('Enter the cost of this dish: '))
                    menu[dish][1] = cost
                    print('\nCost updated!\n')
                    select = input('Press Y to update cost of another dish. Press anything else to go back.\n').casefold()

                except ValueError:
                    print('\nError! Please enter a valid number for servings\n')
                except KeyError:
                    print('\nError! Please enter the correct dish name.\n')

            outfile = open(file,'w')
            outfile.write(str(menu))
            outfile.close()

        select = ''
        while select != '0':

            select = input('Press 1 for Breakfast\nPress 2 for Lunch\nPress 3 for Dinner\nPress 0 to go back\n')

            if select == '1':
                costChanger(breakfast)
                
            elif select == '2':
                costChanger(lunch)

            elif select == '3':
                costChanger(dinner)

            elif select == '0':
                pass

            else:
                print('Please select from the menu.\n')

    select = ''
    while select != '0':
        
        select = input('Press 1 to view the menu\nPress 2 to add new or update existing the menu items\nPress 3 to remove menu items\nPress 4 to change servings available\nPress 5 to change cost of dishes\nPress 0 to go back to the main menu.\n')
        
        if select == '1':
            view(breakfast,lunch,dinner)
        elif select == '2':
            update(breakfast,lunch,dinner)
        elif select == '3':
            remove(breakfast,lunch,dinner)
        elif select == '4':
            servings(breakfast,lunch,dinner)
        elif select == '5':
            cost(breakfast,lunch,dinner)
        elif select == '0':
            pass
        else:
            print('Please select from the menu.\n')
            
def pos(orders,breakfast,lunch,dinner,sales):

    print('POS System'.center(70))
    print('*'*70 + '\n')

    import time

    infile = open(orders)
    orderNo = int(infile.read())
    infile.close()

    select = 'y'
    while select == 'y' and ('08:30' < time.strftime('%H:%M') < '23:59'):
    
        # Main Heading
        receipt = "{:30} Hassan's Cafe\n".format('')
        receipt += '*'*80 + '\n'

        # Order No
        receipt += '{:30} Order No: {}\n'.format('',orderNo)

        # Time and User
        username = input("Enter user's name: \n")
        time_str = time.strftime('%x at %R', time.localtime())
        receipt += 'User: {:46} Time: {}\n'.format(username, time_str)
        receipt += '.'*80 + '\n'

        # Field Headings
        receipt += '{:30}{:20}{:20}{:20}\n'.format('Dish', 'Quantity', 'Rate', 'Amount')
        receipt += '.'*80 + '\n'

        # Field Entry
        net = 0
        user = 'y'
        sale = {orderNo:[]}
        while user == 'y':

            if '08:30' < time.strftime('%H:%M') < '13:00':
                infile = open(breakfast)
                availableMenu = eval(infile.read())
                infile.close()
                print('Breakfast Menu Available.')
                menuFile = breakfast

            elif '13:00' < time.strftime('%H:%M') < '18:00':
                infile = open(lunch)
                availableMenu = eval(infile.read())
                infile.close()
                print('Lunch Menu Available')
                menuFile = lunch

            elif '18:00' < time.strftime('%H:%M') < '23:59':
                infile = open(dinner)
                availableMenu = eval(infile.read())
                infile.close()
                print('Dinner Menu Available')
                menuFile = dinner

            try:
                dish = input('Enter dish: ')
                quantity = int(input('Enter quantity: '))
                if quantity <= (availableMenu[dish][0]):
                    availableMenu[dish][0] -= quantity
                    availableMenu[dish][2] += quantity
                    rate = availableMenu[dish][1]
                    amount = rate * quantity
                    receipt += '\n{:30.25}{:8}{:16}{:22}'.format(dish.title(), quantity, rate, amount)

                    outfile = open(menuFile,'w')
                    outfile.write(str(availableMenu))
                    outfile.close()

                else:
                    print('Not enough available.')
                                                                                                                                                                                                                                                     
            except ValueError:
                print('\nError! Please enter a valid number for quantity\n')      
            except (UnboundLocalError,KeyError):
                print('\nError! Please enter the correct dish name\n')                                                                             
       
                   else:
                        #updating net amount for later tax processing.
                net +=      amount
                                                                                                                                              
                #creat                     ing a record of sale
                sale[orderNo].append({dish:[quantity,rate,amount]})

                #prompt to add another item
                user = input('\nEnter next item? y/n: ').casefold()

        # Totalling
        else:
            tax_rate = 0.13
            tax = net * tax_rate
            total = net + tax

            receipt += '\n' + '-'*80 + '\n'
            receipt += '\n{0:51}{1:10}{2:15}'.format('', 'Net: ', net)
            receipt += '\n{0:51}{1:10}{2:15}'.format('', 'GST: ', tax) + '\n'
            receipt += '\n{0:51}{1:10}{2:15}'.format('', 'Total: ', total)

        #updating record of sale with tax and total amount
        sale[orderNo].append([tax,total])

        #writing record of sale to file
        outfile = open(sales,'a')
        outfile.write(str(sale)+'\n')
        outfile.close()

        #incrementing order number for next order
        orderNo += 1

        #recording order no on file
        outfile = open(orders,'w')
        outfile.write(str(orderNo))
        outfile.close

        #creating a unique filename for receipt printing
        uniqueID = time.strftime('%F %H%M%S', time.localtime()) + ' #{}'.format(orderNo)
        filename = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//Receipts//{}.txt'.format(uniqueID)
        
        #writing the receipt to the file
        outfile = open(filename,'w')
        outfile.write(receipt)
        outfile.close()

        #printing receipt on terminal for customer satisfaction
        print(receipt)

        #prompt to take another order
        select = input('\nPress Y to make another entry. Press anything else to go back.\n').casefold()
    
    else:
        print('Restaurant Closed.\n')

def feedback(feedback_file):
    
    print('Feedback'.center(30))
    print('*'*30 + '\n')

    def add(feedback_file):
        
        try:
            orderNo = int(input('\nEnter Order No.: '))
            customer = input('Enter customer name: ')
            feedback = input('Enter feedback here: ')
            print()

        except ValueError:
            print('\nPlease enter a valid order number\n')

        else:
            dict = {orderNo:[customer,feedback]}

            outfile = open(feedback_file,'a')
            outfile.write(str(dict) + '\n')
            outfile.close()
    
    def view(feedback_file):
        infile = open(feedback_file)
        for record in infile:
            record = eval(record)
            for orderNo,customerFeedback in record.items():
                print('Order No.: {}\nCustomer Name: {}\nRemarks:\n{}\n\n'.format(orderNo,customerFeedback[0],customerFeedback[1]))
        infile.close()

    select = ''
    while select != '0':

        select = input('Press 1 to add feedback\nPress 2 to view feedbacks\nPress 0 to go back to the main menu\n')

        if select == '1':
            add(feedback_file)
        elif select == '2':
            view(feedback_file)
        elif select == '0':
            break
        else:
            print('Please select from the given menu.\n')

def history(sales):
    
    print('Sale History'.center(100))
    print('*'*100 + '\n')
    
    infile = open(sales)
    for record in infile:
        print(record)
    infile.close()

def stats(breakfast,lunch,dinner):

    def printer(menu):
        infile = open(menu)
        menu = eval(infile.read())
        infile.close()

        print('\n{:40}{}\n'.format('Dish','Items Sold'))

        for dish,data in menu.items():
            print('{:40}{}'.format(dish.title(),data[2]))
        print()


    print('Stats'.center(50))
    print('*'*50 + '\n')

    select = ''
    while select != '0':

        select = input('Press 1 for Breakfast\nPress 2 for Lunch\nPress 3 for Dinner\nPress 0 to go back to the main menu\n')

        if select == '1':
            menu = breakfast
            print('Breakfast Menu'.center(50))
            print('^'*50)
            printer(menu)
        elif select == '2':
            menu = lunch
            print('Lunch Menu'.center(50))
            print('^'*50)
            printer(menu)
        elif select == '3':
            menu = dinner
            print('Dinner Menu'.center(50))
            print('^'*50)
            printer(menu)
        elif select == '0':
            pass
        else:
            print('\nPlease select a menu.\n')


#Driver's code
inventory_file = "C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//inventory.txt"
breakfast = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//menu_breakfast.txt'
lunch = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//menu_lunch.txt'
dinner = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//menu_dinner.txt'
orders = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//orders.txt'
sales = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//sales.txt'
feedback_file = 'C:/Users//sahir//OneDrive//Documents//Personal//Usman Institute of Technology University//23FA-CS//Semester I//CSC102 - Programming Fundamentals - FAK//Projects//Final//feedback_file.txt'

restaurant(inventory_file,breakfast,lunch,dinner,orders,sales,feedback_file)