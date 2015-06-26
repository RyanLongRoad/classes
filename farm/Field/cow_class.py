from animal_class import *

class Cow(Animal):
    """ A potato crop"""

    def __init__(self):
        #calls the parent/superclass with default values for growth rate, food need and water need.
        super().__init__(1,6,6,10,"Dave The Cow")
        self._type = "Cow"
        
    #overrid grow method for subclass
        def grow(self,food,water):
            if food >= self._food_need and water >= self._water_need:
                
                if self._status == "New Born" and water > self._water_need:
                    self._growth += self._growth_rate * 1.5
                    
                elif self.status == "Baby" and water > self._water_need:
                    self._growth += self._growth_rate * 1.2
                    
                else:
                    self._growth += self._growth_rate
            #increament days growing
                    self._days_growing += 1
                    self._update_status()
                    


def main():
    cow_animal = Cow()
    print(cow_animal.report())
    manual_grow(cow_animal,1)
    print(cow_animal.report())
    manual_grow(cow_animal,1)
    print(cow_animal.report())

if __name__ =="__main__":
    main()
        
        
