from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """ Creates a group of radio buttons from a list"""
    #constructor
    def __init__(self, label, instruction, button_list):
        super().__init__()

        #create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()

        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set default value for the check item

        self.radio_button_list[0].setChecked(True)

        #cretae the layout for the radio buttons and add them to a group
        self.radio_button_layout = QVBoxLayout()

        #add buttons to the layput and button group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter += 1

        #add radio buttons to the group box
        self.radio_group_box.setLayout(self.radio_button_layout)

        #create a layout for the whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        #set the layout for this widget

        self.setLayout(self.main_layout)

#method to find out the selected button

    def selected_button(self):
        return self.radio_button_group.checkedId()
    
