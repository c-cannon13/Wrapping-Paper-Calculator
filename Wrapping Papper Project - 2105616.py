from cgitb import text
import enum
from fileinput import filename
from glob import glob
from importlib.metadata import entry_points
from operator import length_hint
import string
from tkinter import *
from tokenize import Double
from turtle import color
from webbrowser import get

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


global bow_choice
global card_choice
global card_message
global paper_type
global length 
global width 
global height
global paper_cost
global total_paper
global total_bow
global total_card
global messsage_textbox

total_paper = 0
paper_cost = 0
total_bow = 0
total_card = 0
gift_shape = shape.cube    
paper_type = type.cheap
paper_colour = colour.purple
bow_choice = add_bow.no
card_choice = add_card.no
card_message = ("")
length = 0
width = 0
height = 0

main_window = Tk()
main_window.title("Gift Wrapping")
main_window.config(bg="#E1BEE7")


create_canvas_cheap = Canvas(main_window)
create_canvas_cheap.grid(row=2, column=5)

cheap_label = Label(main_window, text = "cheap - 40p per cm2")
cheap_label.grid(row=3, column=5)
cheap_label.config(bg="#E1BEE7")

for xAxis in range(8):
  for yAxis in range(12):
    create_canvas_cheap.create_polygon(50*xAxis+10, 25*yAxis, 50*xAxis+40, 25*yAxis, 50*xAxis+50, 25*yAxis+25, 50*xAxis, 25*yAxis+25, outline="black", fill="#52307c")


create_canvas_expensive = Canvas(main_window)
create_canvas_expensive.grid(row=5, column=5)

expensive_label = Label(main_window, text = "expensive - 75p per cm2")
expensive_label.grid(row=6, column=5)
expensive_label.config(bg="#E1BEE7")

create_canvas_expensive.create_rectangle(0, 0, 50, 50, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(25, 25, 75, 75, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(50, 50, 100, 100, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(75, 75, 125, 125, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(250, 0, 200, 50, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(175, 25, 225, 75, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(150, 50, 200, 100, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(125, 75, 175, 125, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(0, 200, 50, 250, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(25, 175, 75, 225, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(50, 150, 100, 200, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(75, 125, 125, 175, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(250, 200, 200, 250, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(175, 175, 225, 225, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(150, 150, 200, 200, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(125, 125, 175, 175, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(100, 100, 150, 150, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(250, 0, 300, 50, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(275, 25, 325, 75, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(300, 50, 350, 100, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(325, 75, 375, 125, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(250, 200, 300, 250, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(275, 175, 325, 225, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(300, 150, 350, 200, outline="#52307c", fill="#52307c")
create_canvas_expensive.create_rectangle(325, 125, 375, 175, outline="#52307c", fill="white")
create_canvas_expensive.create_rectangle(350, 100, 400, 150, outline="#52307c", fill="#52307c")


main_window_label = Label(main_window, text = "Gift Wrapping")
main_window_label.grid(row=0, column=3, columnspan=2)
main_window_label.config(font=15, bg="#E1BEE7")


object_submain_label = Label(main_window, text = "Choose the shape of the gift")
object_submain_label.grid(row=1, column=1, columnspan=1)
object_submain_label.config(bg="#E1BEE7")

object_list = ("Cube", "Cuboid", "Cylinder")
variable = StringVar()
variable.set(object_list[2])
object_choice = OptionMenu(main_window, variable, *object_list)
object_choice.grid(row=1, column=2, columnspan=1)

if object_choice == "Cube":
    gift_shape = shape.cube
elif object_choice == "Cuboid":
    gift_shape = shape.cuboid
elif object_choice == "Cylinder":
    gift_shape = shape.cylinder


size_label = Label(main_window, text = "Enter gift dimensions in cm (length, width, height)")
size_label.grid(row=2, column=1, columnspan=1)
size_label.config(bg="#E1BEE7")

length_enter = Entry(main_window)
length_enter.grid(row=2, column=2, columnspan=1)

width_enter = Entry(main_window)
width_enter.grid(row=2, column=3, columnspan=1)

height_enter = Entry(main_window)
height_enter.grid(row=2, column=4, columnspan=1)


paper_label = Label(main_window, text = "Choose a wrapping paper")
paper_label.grid(row=3, column=1, columnspan=1)
paper_label.config(bg="#E1BEE7")

paper_list = ("Cheap", "Expensive")
variable_paper = StringVar()
variable_paper.set(paper_list[1])
paper_choice = OptionMenu(main_window, variable_paper, *paper_list)
paper_choice.grid(row=3, column=2, columnspan=1)


colour_label = Label(main_window, text = "Choose a colour forwrapping paper ")
colour_label.grid(row=4, column=1, columnspan=1)
colour_label.config(bg="#E1BEE7")

colour_list = ("Purple", "Gray", "Blue", "Green", "Red", "Gold")
variable_colour = StringVar()
variable_colour.set(colour_list[5])
colour_choice = OptionMenu(main_window, variable_colour, *colour_list)
colour_choice.grid(row=4, column=2, columnspan=1)

if colour_choice == "Purple":
    paper_colour = colour.purple
elif colour_choice == "Gray":
    paper_colour = colour.gray
elif colour_choice == "Blue":
    paper_colour = colour.blue
elif colour_choice == "Green":
    paper_colour = colour.green
elif colour_choice == "Red":
    paper_colour = colour.red
elif colour_choice == "Gold":
    paper_colour = colour.gold


def bow_yes():
    bow_choice = add_bow.yes

bow_label = Label(main_window, text = "Would you like to add a bow?")
bow_label.grid(row=5, column=1, columnspan=1)
bow_label.config(bg="#E1BEE7")

var1 = IntVar()
Checkbutton(main_window, text="Yes", variable=var1, command=bow_yes, bg="#E1BEE7").grid(row=5, column=2, columnspan=1)


def card_yes():
    global messsage_textbox

    card_choice = add_card.yes

    message_label = Label(main_window, text = "Please enter your message")
    message_label.grid(row=6, column=3, columnspan=1)
    message_label.config(bg="#E1BEE7")

    messsage_textbox = Entry(main_window)
    messsage_textbox.grid(row=6, column=4, columnspan=1)
    card_message = messsage_textbox

card_label = Label(main_window, text = "Would you like to add a card?")
card_label.grid(row=6, column=1, columnspan=1)
card_label.config(bg="#E1BEE7")

var2 = IntVar()
Checkbutton(main_window, text="Yes", variable=var2, command=card_yes, bg="#E1BEE7").grid(row=6, column=2, columnspan=1)


def total_cost():      
    global total
    global paper_cost
    global total_bow
    global height
    global width
    global length
    global total_card
    global total_paper
    global var1
    global var2
    global messsage_textbox


    if variable_paper.get() == "Cheap":
        paper_cost = 0.4
    elif variable_paper.get() == "Expensive":
        paper_cost = 0.75
       

    str_length_num = length_enter.get()
    try:
        length = int(str_length_num)
        pass
    except ValueError:
        size_label = Label(text = "A value is wrong. Please try again")

    str_width_num = width_enter.get()
    try:
        width = int(str_width_num)
        pass
    except ValueError:
        size_label = Label(text = "A value is wrong. Please try again")

    str_height_num = height_enter.get()
    try:
        height= int(str_height_num)
        pass
    except ValueError:
        size_label = Label(text = "A value is wrong. Please try again")


    if var1.get() == 1:
        total_bow = 1.5

    if var2.get() == 1:
        message_length = len(messsage_textbox.get())
        total_card = message_length*0.02 + 0.5


    total_paper_width = height + height + width + 6
    total_paper_height = (height + length + 3)*2
    total_paper_size = total_paper_height*total_paper_width
    total_paper = (total_paper_size*paper_cost)/100


    total = str(total_paper + total_bow + total_card)
    total_message = Label(main_window, text = "Your total is £" + total + " Would you like a receipt?")
    total_message.grid(row=7, column=2, columnspan=2)
    total_message.config(bg="#E1BEE7")

    receipt_button = Button(main_window, text = "Receipt", command= receipt)
    receipt_button.grid(row=7, column=4, columnspan=1)

filename = "receipt.txt"

def receipt():
    output_file = open(filename, "a")
    output_file.write(str(paper_cost))
    output_file.write("\n")
    output_file.write(str(total_paper))
    output_file.write("\n")
    output_file.write(str(total_bow))
    output_file.write("\n")
    output_file.write(str(total_card))
    output_file.write("\n")
    output_file.write(total)
    output_file.close


total_button = Button(main_window, text = "Total", command= total_cost)
total_button.grid(row=7, column=1, columnspan=1)

main_window.mainloop()