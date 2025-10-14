#from asyncio.windows_events import NULL
#from curses.textpad import Textbox
import enum
from importlib.metadata import entry_points
from operator import length_hint
import string
from tkinter import *
from turtle import color

class shape(enum.Enum):
    cube = 1
    cuboid = 2
    cylinder = 3

class type(enum.Enum):
    cheap = 1
    expensive = 2

class colour(enum.Enum):
    purple = 1
    gray = 2
    blue = 3
    green = 4
    red = 5
    gold = 6

class add_bow(enum.Enum):
    yes = 1
    no = 2

class add_card(enum.Enum):
    yes = 1
    no = 2

    
gift_shape = shape.cube    
paper_type = type.cheap
paper_colour = colour.purple
bow_choice = add_bow.no
card_choice = add_card.no

card_message = ("")
length = 0
width = 0
height = 0


def open_main_window():
    object_window.title("Gift Wrapping")

    object_main_label = Label(object_window, text = "Gift Wrapping")
    object_main_label.grid(row=0, column=2, columnspan=2)
    object_main_label.config(font=85)

    object_submain_label = Label(object_window, text = "Choose the shape of the gift")
    object_submain_label.grid(row=1, column=2, columnspan=2)

    cube_buttion = Button(object_window, image = cube_btn, command=cube_button_selected)
    cube_buttion.grid(row=2, column=0, columnspan=2)

    cube_label = Label(object_window, text = "Cube")
    cube_label.grid(row=3, column=0, columnspan=2)

    cuboid_buttion = Button(object_window, image = cuboid_btn, command=cuboid_button_selected)
    cuboid_buttion.grid(row=2, column=2, columnspan=2)

    cuboid_label = Label(object_window, text = "Cuboid")
    cuboid_label.grid(row=3, column=2, columnspan=2)

    cylinder_buttion = Button(object_window, image = cylinder_btn, command=cylinder_button_selected)
    cylinder_buttion.grid(row=2, column=4, columnspan=2)

    cylinder_label = Label(object_window, text = "Cylinder")
    cylinder_label.grid(row=3, column=4, columnspan=2)

def cube_button_selected():
    gift_shape = shape.cube
    open_paper_window()

def cuboid_button_selected():
    gift_shape = shape.cuboid
    open_paper_window()

def cylinder_button_selected():
    gift_shape = shape.cylinder
    open_paper_window()


def open_paper_window():
    global paper_window
    global cheap_btn
    global expensive_btn    
    paper_window = Toplevel(object_window)
    paper_window.title("Gift Wrapping") 
    
    paper_main_label = Label(paper_window, text = "Gift Wrapping")
    paper_main_label.grid(row=0, column=2, columnspan=2)
    paper_main_label.config(font=85)

    paper_submain_label = Label(paper_window, text = "Choose the type wrapping paper")
    paper_submain_label.grid(row=1, column=2, columnspan=2)

    cheap_buttion = Button(paper_window, image = cheap_btn, command=cheap_button_selected)
    cheap_buttion.grid(row=2, column=1, columnspan=2)

    cheap_label = Label(paper_window, text = "Cheap")
    cheap_label.grid(row=3, column=1, columnspan=2)

    expensive_buttion = Button(paper_window, image = expensive_btn, command=expensive_button_selected)
    expensive_buttion.grid(row=2, column=3, columnspan=2)

    expensive_label = Label(paper_window, text = "Expensive")
    expensive_label.grid(row=3, column=3, columnspan=2)

def expensive_button_selected():
    paper_type = type.expensive
    open_colour_window()

def cheap_button_selected():
    paper_type = type.cheap
    open_colour_window()


def open_colour_window():
    global colour_window
    colour_window = Toplevel(paper_window)
    colour_window.title("Gift Wrapping") 

    colour_main_label = Label(colour_window, text = "Gift Wrapping")
    colour_main_label.grid(row=0, column=2, columnspan=2)
    colour_main_label.config(font=85)

    colour_submain_label = Label(colour_window, text = "Choose the wrapping paper colour")
    colour_submain_label.grid(row=1, column=2, columnspan=2)
    
    purple_buttion = Button(colour_window, background = "purple", command=purple_button_selected, text = "Purple")
    purple_buttion.grid(row=2, column=1, columnspan=2)
   
    gray_buttion = Button(colour_window, background = "DarkSlateGray4", command=gray_button_selected, text = "Gray")
    gray_buttion.grid(row=2, column=2, columnspan=2)
   
    blue_buttion = Button(colour_window, background = "deep sky blue", command=blue_button_selected, text = "Blue")
    blue_buttion.grid(row=2, column=3, columnspan=2)
   
    green_buttion = Button(colour_window, background = "light sea green", command=green_button_selected, text = "Green")
    green_buttion.grid(row=3, column=1, columnspan=2)
   
    red_buttion = Button(colour_window, background = "VioletRed2", command=red_button_selected, text = "Red")
    red_buttion.grid(row=3, column=2, columnspan=2)
   
    gold_buttion = Button(colour_window, background = "gold", command=gold_button_selected, text = "Gold")
    gold_buttion.grid(row=3, column=3, columnspan=2)

def purple_button_selected():
    paper_colour = colour.purple
    open_bow_window()

def gray_button_selected():
    paper_colour = colour.gray
    open_bow_window()

def blue_button_selected():
    paper_colour = colour.blue
    open_bow_window()

def green_button_selected():
    paper_colour = colour.green
    open_bow_window()

def red_button_selected():
    paper_colour = colour.red
    open_bow_window()

def gold_button_selected():
    paper_colour = colour.gold
    open_bow_window()


def open_bow_window():
    global bow_window
    bow_window = Toplevel(colour_window)
    bow_window.title("Gift Wrapping") 

    bow_main_label = Label(bow_window, text = "Gift Wrapping")
    bow_main_label.grid(row=0, column=2, columnspan=2)
    bow_main_label.config(font=85) 
    
    bow_submain_label = Label(bow_window, text = "Would you like to add a bow?")
    bow_submain_label.grid(row=1, column=2, columnspan=2)

    yes_bow_buttion  = Button(bow_window, command=yes_bow_button_selected, text = "yes")
    yes_bow_buttion.grid(row=2, column=1, columnspan=2)
   
    no_bow_buttion = Button(bow_window, command=no_bow_button_selected, text = "no")
    no_bow_buttion.grid(row=2, column=2, columnspan=2)

def yes_bow_button_selected():
    bow_choice = add_bow.yes
    open_card_window()

def no_bow_button_selected():
    bow_choice = add_bow.no
    open_card_window()


def open_card_window():
    global card_window
    card_window = Toplevel(bow_window)
    card_window.title("Gift Wrapping") 

    card_main_label = Label(card_window, text = "Gift Wrapping")
    card_main_label.grid(row=0, column=2, columnspan=2)
    card_main_label.config(font=85) 
    
    card_submain_label = Label(card_window, text = "Would you like to add a card?")
    card_submain_label.grid(row=1, column=2, columnspan=2)

    yes_card_buttion  = Button(card_window, command=yes_bow_button_selected, text = "yes")
    yes_card_buttion.grid(row=2, column=1, columnspan=2)
   
    no_card_buttion = Button(card_window, command=no_bow_button_selected, text = "no")
    no_card_buttion.grid(row=2, column=2, columnspan=2)

def yes_card_button_selected():
    card_choice = add_card.yes
    open_message_window()

def no_card_button_selected():
    card_choice = add_card.no
    open_cost_window()


def open_message_window():
    global message_window
    message_window = Toplevel(card_window)
    message_window.title("Gift Wrapping") 

    message_main_label = Label(message_window, text = "Gift Wrapping")
    message_main_label.grid(row=0, column=2, columnspan=2)
    message_main_label.config(font=85) 
    
    message_submain_label = Label(message_window, text = "Please enter card message")
    message_submain_label.grid(row=1, column=2, columnspan=2)

    message_textbox = Entry(message_window)
    message_textbox.grid(row=2, column=2, columnspan=2)

    message_buttion = Button(message_window, command=open_cost_window, text = "total")
    message_buttion.grid(row=3, column=2, columnspan=2)

    card_message = message_textbox.get


def open_cost_window():
    global bow_window
    card_window = Toplevel(colour_window)
    card_window.title("Gift Wrapping") 

    card_main_label = Label(card_window, text = "Gift Wrapping")
    card_main_label.grid(row=0, column=2, columnspan=2)
    card_main_label.config(font=85) 
    
    card_submain_label = Label(card_window, text = "your total cost is: ")
    card_submain_label.grid(row=1, column=2, columnspan=2)


#create main window
object_window = Tk()

#load button images
cube_btn= PhotoImage(file='Cube.png')
cuboid_btn= PhotoImage(file='Cuboid.png')
cylinder_btn= PhotoImage(file='Cylinder.png')

cheap_btn= PhotoImage(file='Cheap.png')
expensive_btn= PhotoImage(file='Expensive.png')

#set up main window
open_main_window()

#start main window loop
object_window.mainloop()