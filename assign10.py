

country_list = ['United States','mexico','Denmark','CANADA','UK','Austrailia','ca','Us','wY']

codes ={
    'United States':'US',
    
    'Mexico':'MX',
    
    'Canada':'CA',
    
    'Great Britain':'UK',
    
    'Australia': 'AU',}


print("This is the old list!")
print()
print(country_list)
print()


for C in range(len(country_list)):
    
    country = codes.get(country_list[C].title(),country_list[C])
    
    if country in codes.values():
        print ("The entry from: "+country_list[C]+" was updated to: "+country+".")
        country_list[C] = country
        
    else:
        print("This country was not updated: "+country_list[C])
print()        
print('Here is your new list!')
print()
print(country_list) 
