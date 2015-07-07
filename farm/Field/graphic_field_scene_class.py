from PyQt4.QtGui import *

from field_class import *
from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_crop_item_class import *
from graphic_sheep_item_class import *

import field_resources

class FieldGraphicScene(QGraphicsScene):
    """this class provides a scene to manage items in the field"""

    #constructor
    def __init__(self,
