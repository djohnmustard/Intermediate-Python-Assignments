classes = 0
courses = ["Chemistry", "Biology", "Algebra", "Economics", "Python"]
while classes != 5:
    print("Welcome to the Add/Drop course app.")
    print()
    print("If you want to cancel, please type 5 to Quit the program!")
    print()
    print("Please type 1 to show the courses you are currently enrolled in, 2 for Add, 3 for Drop, or 4 to Cancel:")
    print()
    
    
    classes = int(input("Pick a number from the list:"))
    
    if classes == 1:
        print ("You are currently enrolled in the following classes: ")
        current = 0
        
        if len(courses) > 0:
            while current < len(courses):
                print(current, ".", courses[current])
                current = current + 1
        else:
            print("You are not currently enrolled in a course.")
            print()
            
    if classes == 2:
       
        newest_name = input("Type in a course name to add: Chemistry, Biology, Algebra, Economics, Python : ")
        courses.append(newest_name)
        print("Added!")
     
        if newest_name is courses:
            print("Sorry, you are already enrolled in that course")
            print()

            
        
    elif classes == 3:
        del_name = input("What course would you like to Drop?: ")
        
        if del_name in courses:
            item_number = courses.index(del_name)
            del courses[item_number]
            print()
            print("Dropped!")
            print()
        
        else:
            print(del_name, "Sorry, you must be enrolled in a course to drop it.")
            print()
            
    elif classes == 4:
        old_name = input("What course would you like to cancel?: ")
       
        
        if old_name in courses:
            item_number = courses.index(old_name)
            new_name = input("What is the new course you would like to swap it with?: ")
            courses[item_number] = new_name
            
        else:
            print(old_name, "wasn't found!")
            print()

print("Goodbye!")
quit()

