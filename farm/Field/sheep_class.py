from animal_class import *

class Sheep(Animal):
    """ A potato crop"""

    def __init__(self):
        #calls the parent/superclass with default values for growth rate, food need and water need.
        super().__init__(1,6,6,10,"Dave The Sheep")
        self._type = "Sheep"
        
    #overrid grow method for subclass
        def grow(self,food,water):
            if food >= self._food_need and water >= self._water_need:
                
                if self._status == "Baby" and water > self._water_need:
                    self._growth += self._growth_rate * 1.5
                    
                elif self.status == "Young" and water > self._water_need:
                    self._growth += self._growth_rate * 1.2
                    
                else:
                    self._growth += self._growth_rate
            #increament days growing
                    self._days_growing += 1
                    self._update_status()
                    


def main():
    sheep_animal = Sheep()
    print(sheep_animal.report())
    manual_grow(sheep_animal,1)
    print(sheep_animal.report())
    manual_grow(sheep_animal,1)
    print(sheep_animal.report())

if __name__ =="__main__":
    main()
        
        
