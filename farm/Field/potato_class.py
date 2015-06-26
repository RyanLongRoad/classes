from crop_class import *

class Potato(Crop):
    """ A potato crop"""

    def __init__(self):
        #calls the parent/superclass with default values for growth rate, light need and water need.
        super().__init__(1,3,6)
        self._type = "Potato"
        
    #overrid grow method for subclass
        def grow(self,light,water):
            if light >= self._light_need and water >= self._water_need:
                
                if self._status == "Seedling" and water > self._water_need:
                    self._growth += self._growth_rate * 1.5
                    
                elif self.status == "Young" and water > self._water_need:
                    self._growth += self._growth_rate * 1.2
                    
                else:
                    self._growth += self._growth_rate
            #increament days growing
                    self._days_growing += 1
                    self._update_status()
                    


def main():
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop,1)
    print(potato_crop.report())
    manual_grow(potato_crop,1)
    print(potato_crop.report())

if __name__ =="__main__":
    main()
        
        
