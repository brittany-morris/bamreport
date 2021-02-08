#!/usr/bin/env python3

from tkinter import *
from tkcalendar import * 
from textwrap import TextWrapper 

from reportlab.pdfgen.canvas import Canvas 

#create a blank window called root
root = Tk()
root.title('Bam Reporting')

#set the size
root.geometry('1000x1000')

#create a label widget
#put it on a grid to determine where the label lies on the window
lbl = Label(root, text = "Welcome To Bam Reporting")
lbl.grid(column = 0, row = 0)



#making a date entry widget

select_date_lbl = Label(root, text = "Please select the date").grid(column = 0, row = 1) 

cal = Calendar(root, selectmode = "day", year = 2021, month = 2, day = 5)
cal.grid(column = 0 , row = 2)

def grab_date():
    cal_label.config(text = cal.get_date())

cal_button = Button(root, text = "Select Date", command = grab_date)
cal_button.grid(column = 0, row = 3)

cal_label = Label(root, text = "")
cal_label.grid(column = 0, row = 4)



#creating a dropdown menu
def show2():
    lbl2 = Label(root, text=clicked1.get()).grid(column = 1, row = 3)

clicked1 = StringVar()
clicked1.set("Select Options")

options1 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked1, *options1)
drop.grid(column = 1, row = 1)

#displays selection
myButton = Button(root, text = "show selection", command = show2).grid(column = 1, row = 2)



#creating a dropdown menu
def show3():
    lbl3 = Label(root, text=clicked2.get()).grid(column = 2, row = 3)

clicked2 = StringVar()
clicked2.set("Select Options")

options2 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked2, *options2)
drop.grid(column = 2, row = 1)

#displays selection
myButton = Button(root, text = "show selection", command = show3).grid(column = 2, row = 2)



#creating a dropdown menu
def show4():
    lbl4 = Label(root, text=clicked3.get()).grid(column = 3, row = 3)

clicked3 = StringVar()
clicked3.set("Select Options")

options3 = [
        "options",
        "for",
        "dropdown",
        "menu"
]

drop = OptionMenu(root, clicked3, *options3)
drop.grid(column = 3, row = 1)

#displays selection
myButton = Button(root, text = "show selection", command = show4).grid(column = 3, row = 2)

#creating a checkbox for selecting the incident type

typeincidentlbl = Label(root, text = "Select the type of incident (select all that apply)").grid(column = 0, row = 5)

incidentvar1 = IntVar()
incidentvar2 = IntVar()
incidentvar3 = IntVar()
incidentvar4 = IntVar()
incidentvar5 = IntVar()
incidentvar6 = IntVar()
incidentvar7 = IntVar()

type_cb1 = Checkbutton(root, text = "Intellectual Property Theft", variable = incidentvar1, anchor = W).grid(column = 0, row = 6)

type_cb2 = Checkbutton(root, text = "Financial Crime", variable = incidentvar2, anchor = W).grid(column = 0, row = 7)

type_cb3 = Checkbutton(root, text = "Insider Threat", variable = incidentvar3, anchor = W).grid(column = 0, row = 8)

type_cb4 = Checkbutton(root, text = "Destructive Attacks", variable = incidentvar4, anchor = W).grid(column = 0, row = 9)

type_cb5 = Checkbutton(root, text = "Protected Health Information", variable = incidentvar5, anchor = W).grid(column = 0, row = 10)

type_cb6 = Checkbutton(root, text = "Personally Identifiable Information", variable = incidentvar6, anchor = W).grid(column = 0, row = 11)

type_cb7 = Checkbutton(root, text = "Other", variable = incidentvar7, anchor = W).grid(column = 0, row = 12)


#making an input text field
canvas = Canvas("user_input.pdf")
user_in = str() 

input_field = Text(root, height =2, width = 10) 
input_field.grid(column = 4, row =1) 
 
def submit(): 
    global user_in, root 
    user_in = input_field.get(1.0, "end-1c") 
    root.destroy() 
 
submit_button = Button(root, text="submit", command=submit) 
submit_button.grid(column = 4, row = 2) 
root.mainloop() 

user_in_lines = user_in.split('\n') 
wrapper = TextWrapper() 
user_in_wrapped_lines = list() 
 
for line in user_in_lines: 
    user_in_wrapped_lines += wrapper.wrap(line) 

count = 0 
text_object = canvas.beginText(100, 741.89) 
 
for line in user_in_wrapped_lines: 
    text_object.textLine(line) 
    count += 1 
    if count == 45: 
       canvas.drawText(text_object) 
       canvas.showPage() 
       text_object = canvas.beginText(100, 741.89) 
       count = 0 
 
canvas.drawText(text_object) 
 
# Save the pdf file 
canvas.showPage() 
canvas.save() 


#call the mainloop funtion to run the program
root.mainloop()