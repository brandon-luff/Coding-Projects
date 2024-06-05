## Defining class Bicycle to contain all functions related to the objects properties
class Bicycle():
    
    ## Initializing the default properties when the class is initialized
    ## Should update this allow user to pass parameters to the def
    def __init__(self, wheels = 2, color = 'blue', gears = 6, miles = 0):
        self.wheels = wheels
        self.color = color
        self.gears = gears
        self.miles = miles
        
    ## The folliwing functions are to return and save values of specific bikes
    ## as well as increment the miles and be able to change to amount of wheels on the bike
    def add_miles(self):
        self.miles = self.miles + 1
        
    def change_wheels(self):
        self.wheels = input("How many wheels on the bike?" + "\n")
    
    def see_wheels(self):
        return self.wheels
    
    def see_color(self):
        return self.color
    
    def see_gears(self):
        return self.gears
    
    def see_miles(self):
        return self.miles
        
        
## Defining class Owner to contain all functions related to the objects properties
class Owner():
    
    ## Initializing the default properties when the class is initialized
    def __init__(self, prev_owners = [], list_name = None, description = None, owner = None):
        self.prev_owners = prev_owners
        self.list_name = 'Owner History'
        self.description = 'A list of all previous owners of the bike'
        self.owner = owner
    
    ## The folliwing functions are to return and save values of specific Owners
    ## as well as allow the user to add previous owners to a list and display those owners.
    ## Also returns values to store data of specific owners. The current owner can be updated
    def add_owners(self):
        add = True
        i = 0
        while add == True:
            self.prev_owners.append(input("Add a previous owner to the list: "))
            check = input("Would you like to append another? (Yes/No)" + "\n" + 
                          "Must be spelled as indicated" + "\n")
            check = check.title()
            if check == "Yes":
                add = True
                i += 1
            else:
                add = False
                
    def display_owners(self):
        check = int(input("How would you like to display the previous owners?" + "\n" + 
                      "Enter 0 to increment from 0..." + "\n" + "Enter 1 to increment from 1..." +
                      "\n" + "Enter anything else to show no increments..." + "\n"))
        if check == 0:
            for i, item in enumerate(self.prev_owners, 0): 
                print("\n" + "\t" + str(i) + ". " + str(item))
                
        elif check == 1:
            for i, item in enumerate(self.prev_owners, 1): 
                print("\n" + "\t" + str(i) + ". " + str(item))
                
        else:
            for i in self.prev_owners: 
                print("\n" + "\t" + i)
                
        print("\n" + "\t" + "Current Owner: " + str(self.owner))
                
    def see_list_legnth(self):
        length = len(self.prev_owners)
        return length
    
    def see_desc(self):
        return self.description
    
    def update_owner(self):
        self.owner = input("Name of the current owner of the Bike:" + "\n ")
        return self.owner
    
    def see_owner(self):
        return self.owner
    
## Class run utillizes the funtions above to run the program as intended and
## print the neccesary information
class run():
    
    ## intializing the classes
    B = Bicycle()
    O = Owner()
    
    ##obtaining the needed inputs from the user
    B.add_miles()
    B.change_wheels()
    O.add_owners()
    O.update_owner()
    
    ## printing the required fields
    print("\n" + "Displaying properties of the objects to show functionality:")
    print("Wheels: " + str(B.see_wheels()))
    print("Color: " + str(B.see_color()))
    print("Gears: " + str(B.see_gears()))
    print("Miles: " + str(B.see_miles()))
    print("Number of prior owners: " + str(O.see_list_legnth()))
    print("Description: " + str(O.see_desc()))
    print("Number of prior owners: " + str(O.see_list_legnth()))
    print("Current Owner: " + str(O.see_owner()))
    
    ##prints the previous owners
    O.display_owners()
    
    
    
        
    
                      
        
            

            















        