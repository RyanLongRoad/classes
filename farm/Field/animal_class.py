import random

class Animal:
    """ A generic animal """

    #constructor

    def __init__(self, growth_rate, water_need, food_need, weight, name):
        self._growth = 0
        self._days_growing = 0
        self._weight = weight
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Unborn"
        self._type = "Generic"
        self._name = name


    def needs(self):
        #return a dictionary containing the food and water needs
        return {'food need':self._food_need,'water need':self._water_need}

    #method to report the provided information wabout the current state of the animal
    def report(self):
        #return a dictionary contain the type, status, growth, days growing, name and weight of the animal
        return{'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing,'name':self._name,'weight':self._weight}

    def _update_status(self):
        
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Baby"
        elif self._growth == 0:
            self._status = "New Born"
            
    
        

    def grow(self,food,water):
        if food>= self._food_need and water>=self._water_need:
            self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()


def auto_grow(animal, days):
    #grow the animal
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal, days):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("That is not an acceptable value. please enter a value between 1 and 10")
                
        except ValueError:
            print("That is not an acceptable value. please enter a value between 1 and 10")

    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print ("please enter a value between 1 and 10")
                
        except ValueError: 
            print("That is not an acceptable value. please enter a value between 1 and 10")
    
    #grow the animal

    animal.grow(food,water)

def display_menu():
    print("1. grow manually")
    print("2. grow automatically over 30 days")
    print("3. report status")
    print("0. Exit program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("That is not an acceptable value. Pick a number from the menu.")

        except ValueError:
            print("That is not an acceptable value. Pick a number from the menu.")
            
    return choice
            

def manage_animal(animal):
    print("this is the animal managment program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal,1)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using my program")
        
        

def main():
    
         
    #instaniate the class
    new_animal = Animal(1,4,3,5,"daisy")
    manage_animal(new_animal)
    


     
if __name__ == "__main__":
    main()



        


        
