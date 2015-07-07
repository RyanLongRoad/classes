from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *

import random
class Field():
    """Simulate a field that can contain animals and crops"""

    #constructor
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())

        return{"crops": crop_report, "animals":animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]

            if needs["water need"] > water:
                water = needs["water need"]

        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]

            if needs["water need"] > water:
                water = needs["water need"]

        return{"food":food,"light":light,"water":water}

    
    def grow(self,light,food,water):
        #grow the crops (light and water are available to all
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light,water)

        if len(self._animals) > 0:
            #grow the aniamls (water available to all animals)
            #food is a total that must be shared
            food_required = 0
            
            #get a total of the food required by the animals in the field
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["food need"]
                
            #if excess food is available it is shared out equally
            if food > food_required:
                addition_food = food - food_required
                food = food_required
            else:
                additional_food = 0
                
            #growing the animals
                for animal in self._animals:
                    #get the animals food needs
                    needs = animal.needs()
                    if food >= needs["food need"]:
                        #removes food for this animal from the total
                        food -= needs["food need"]
                        feed= needs["food need"]
                        #see if there is any additional food to give
                        if additional_food > 0:
                            #removes additonal food for this animal
                            additional_food -= 1
                            #add this feed to he animal
                            feed +=1
                        #grow the animal
                        animal.grow(feed,water)
                    
                        
                    

                

def auto_grow(field,days):
    #grow the field automatically
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light,food,water)

def manual_grow(field):
    #get the lgiht,water and the food values from the user
    valid = False
    while not valid:
        try:
            light = int(input("please enter a value for light(1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("value entered is not valid - please enter another value")
        except ValueError:
            print("value entered is not valid - please enter another value")

    valid = False
    while not valid:
        try:
            water = int(input("please enter a value for water(1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("value entered is not valid - please enter another value")
        except ValueError:
            print("value entered is not valid - please enter another value")
    

        valid = False
        while not valid:
            try:
                food = int(input("please enter a value for food(1-100): "))
                if 1 <= food <= 10:
                    valid = True
                else:
                    print("value entered is not valid - please enter another value")
            except ValueError:
                print("value entered is not valid - please enter another value")

    #grow the field
    field.grow(light,food,water)
        

def display_crops(crop_list):
    print()
    print("The following crops are in this field: ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1

def display_animals(animal_list):
    print()
    
    
    print("the following animals are in this field: ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos +=1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("please select a valid option")

    return selected - 1


def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select an animal: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("please select a valid option")

    return selected - 1

                                   
def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)

def display_crop_menu():
    print()
    print("which crop type would you like to add?")
    print()
    print("1. potato")
    print("2. wheat")
    print()
    print("0. return to main menu")

def main():
    new_field = Field(5,2)
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())
    new_field.add_animal(Sheep("Shaun"))
    new_field.add_animal(Cow("Jim"))
    report = new_field.report_contents()
    #manual_grow(new_field)
    #print(new_field.report_contents())
    auto_grow(new_field,30)
    print(new_field.report_contents())
                

    
if __name__ == "__main__":
    main()
