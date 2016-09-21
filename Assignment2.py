import kivy

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.utils import get_color_from_hex

from ShoppingList1 import *  # import the first ShoppingList1

Builder.load_file('Assignment2.kv')


class MenuScreen(BoxLayout):
    List_Required = 'List Required'  # MENU 1
    List_completed = 'List completed'  # MENU 2
    Add_new_item = 'Add new item...\n\nName:'  # Add new item in to Menu
    Price = 'Price:'
    Priority = 'Priority:'
    Add_Item = 'Add Item'
    Clear = 'Clear'  # Clear the information which have typed
    
    Label_color = get_color_from_hex('#FFFFFF')  # choose the word color
    Label_background_color = get_color_from_hex('#0000FF')  # choose the background color

    Label_background_color1 = get_color_from_hex('#00FFFF')  # choose the background color1
    Label_background_color2 = get_color_from_hex('#FF00FF')  # choose the background color2
    Label_background_color3 = get_color_from_hex('#FFFF00')  # choose the background color3
    Label_background_color4 = get_color_from_hex('#000000')  # choose the background color4

    def func1(self):  # Build list 1
        self.func4()  # Clear the content
        List1,s = required_list()
        self.ids.time0.text = s
        self.ids.time1.text = List1[0]
        self.ids.time2.text = List1[1]
        self.ids.time3.text = List1[2]

    def func2(self):  # Build list 2
        try:
            self.func4()  # Clear the interface content
            List2,s2 = completed_list()
            self.ids.time0.text = s2
            self.ids.time1.text = List2[0]
            self.ids.time2.text = List2[1]
            self.ids.time3.text = List2[2]
        except:
            self.ids.time4.text = 'No completed items'

    def func3(self):  # Build list 3
        self.func4()  # Clear the interface content
        new_item = self.ids.new_item.text
        pricex = self.ids.pricex.text
        priorityx = self.ids.priorityx.text
        # print(new_item,pricex,priorityx)
        if new_item and pricex and priorityx:
            if not new_item.isspace():   # Determine whether the input is space(if not, out of the loop)
                self.ids.time1.text = new_item
            else:
                self.ids.time4.text = 'Input can not be blank'

            if pricex.isdigit():  # Determine whether the input is digit(if so, out of the loop)
                self.ids.time2.text = pricex
            elif float(pricex) < 0:   # Determine whether is the negative number
                self.ids.time4.text = 'Price must be >= $0'
            else:                     # Otherwise the input is invalid, it should be postive
                self.ids.time4.text = 'Invalid input; enter a valid number'

            if priorityx.isdigit():  # Judge the input is all digital
                if priorityx in '123':  # To determine the scope of the priority code
                    self.ids.time3.text = priorityx
                else:
                    self.ids.time4.text = 'Priority must be 1, 2 or 3'
            else:                 # Otherwise the input is invalid, it should be postive
                self.ids.time4.text = 'Invalid input; enter a valid number'

    def func4(self):  # Build list 4
        self.ids.time0.text = ''
        self.ids.time1.text = ''
        self.ids.time2.text = ''
        self.ids.time3.text = ''
        self.ids.time4.text = ''


class ShoppingApp(App):
    def build(self):
        return MenuScreen()

if __name__ == '__main__':
    ShoppingApp().run()

