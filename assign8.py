import os
import sys
students = ["Mick","Keith","Pete","Roger","Sierra","Chelsey"]
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
        
def main(): 
    
    print ("These are the current students in the class: ")
    s = 1
    for student in students: 
                print(str(s) + ": " + student)
                s += 1
    app = input('This is the Class Enrollment App. Type A to Add yourself to the class, or D to Drop: ').upper()
    
    
    
    if app == 'A':
        add = input ("What's your First Name? ")
        add = add.title() 
        if add in students: 
            message = "Oops! You're already in this class!"
        else:
            students.append(add)
            message = "Awesome! Welcome to the class!"
            
            
        
    elif app == 'D': 
        drop = input ("What's your first name? ")
        drop = drop.title()
        if drop not in students:
            message = "Oops! you need to be in the class to drop it!"
            
        else: 
            students.remove(drop) 
            message = "Awesome! You're out of the class!"
            
    else:
        message = "Oops. That's not right."     
    
    return {'app':app, 'message':message}    

process = main() 
while process['app'] != 'c': 
    clearScreen() 
    print(process['message'])
    process = main() 
quit() 
