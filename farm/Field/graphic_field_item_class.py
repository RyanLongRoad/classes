from PyQt4.QtGui import *

class FieldItemGraphicsPixmapItem(QGraphicsPixmapItem):
    """thsi class provides a pixmap item with a preset image for the item"""

    #constructor
    def __init__(self, graphics_list):
        super().__init__()
        self.available_graphics = graphics_list
        self.current_current = QPixmap(self.available_graphics[0])
        self.setPixmap(self.current_graphic.scaledToWidth(25,1))
        self.setFlag(QGrapicsItem.ItemIsMovable) #allows us to move the graphic


    def update_status(self):
        pass
