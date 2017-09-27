
courses = ['chemistry','biology','algebra','economics','python']
        
def main(): 

    print("This is the Class Enrollment App")
    print()
    print("You are currently enrolled in the following classes: ")
    print()
    s = 1
    for course in courses: 
                print(str(s) + ": " + course)
                s += 1
    app = input('Welcome to the Add/Drop App. Please enter A for Add, D for Drop, or C for Cancel: ')
    app = app.lower() 
    
    
    if app == 'a':
        enroll = input ('What class would you like to add? ')
        enroll = enroll.lower() 
        if enroll in courses: 
            message = "Oops! You're already in this class!"
        else:
            courses.append(enroll)
            message = "Awesome! Welcome to the class!"
            
        
    elif app == 'd': 
        drop = input ('What class would you like to drop? ')
        drop = drop.lower()
        if drop not in courses:
            message = "Oops! you need to be in the class to drop it!"
        else: 
            courses.remove(drop) 
            message = "Awesome! You've dropped the course!"
    elif app == 'c': 
        message = "See ya!"
    else:
        message = "Oops. That's not right." 
  
    return {'app':app, 'message':message}
    

process = main() 
while process['app'] != 'c': 
    print(process['message'])
    process = main() 
quit() 



    

