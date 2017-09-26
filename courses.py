classes = 0
namelist = []
while classes != 5:
    print("Welcome to the Add/Drop course app.")
    print()
    print("If you don't want to add a class now, please type 5 to Quit the program!")
    print()
    print("Please type 1 to show currently enrolled Courses, 2 for Add, 3 for Drop, or 4 to Cancel:")
    print()
    
    
    classes = int(input("Pick a number from the list:"))
    
    if classes == 1:
        current = 0
        
        if len(namelist) > 0:
            while current < len(namelist):
                print(current, ".", namelist[current])
                current = current + 1
        else:
            print("You are not currently enrolled in a course.")
            print()
            
    elif classes == 2:
        newest_name = input("Type in a course name to add: Chemistry, Biology, Algebra, Economics, Python : ")
        namelist.append(newest_name)
        
        if newest_name in namelist:
            item_number = namelist.index(newest_name)
            print("Added!")
            print()

        else:
            print(newest_name, "Sorry, you are already enrolled in that course")
            print()
            

            
        
    elif classes == 3:
        del_name = input("What course would you like to Drop?: ")
        
        if del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
            print("Dropped!")
            print()
        
        else:
            print(del_name, "Sorry, you must be enrolled in a course to drop it.")
            print()
            
    elif classes == 4:
        old_name = input("What course would you like to cancel?: ")
       
        
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("What is the new course you would like to swap it with?: ")
            namelist[item_number] = new_name
            
        else:
            print(old_name, "wasn't found!")
            print()

print("Goodbye!")

