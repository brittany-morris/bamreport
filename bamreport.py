#!/usr/bin/env python3

from tkinter import *
from tkcalendar import * 
from textwrap import TextWrapper 
from reportlab.pdfgen.canvas import Canvas 

#create a blank window called root
root = Tk()
root.title('Bam Reporting')

#set the size
root.geometry('1250x900')

#create a label widget
#put it on a grid to determine where the label lies on the window
lbl = Label(root, text = "Welcome To Bam Reporting",font=25)
lbl.grid(column = 0, row = 0)


#Report Type drop Down
def reporttype():
    reporttype_label = Label(root, text=reporttype_click.get()).grid(column = 0, row =3, padx=40, pady=10 )
    global report_type
    report_type = reporttype_click.get()

reporttype_click = StringVar()
reporttype_click.set("Select Report Type")

reporttype_options = [
        "Incident Response Report"
        ]

reporttypedrop = OptionMenu(root, reporttype_click, *reporttype_options)
reporttypedrop.grid(column = 0, row = 1, padx=40, pady=10)

# Report Type Display selection
reporttypebutton = Button(root, text = "show selection", command = reporttype).grid(column = 0, row = 2, padx=40, pady=10)


# Month drop Down
def month():
    month_label = Label(root, text=month_click.get()).grid(column = 1, row = 3, padx=40, pady=10)
    global month_drop
    month_drop = month_click.get()

month_click = StringVar()
month_click.set("Select Month")

month_options = [
        "January", "February", "March", "April", "May", "June", "July", "August",
        "September", "October", "November", "December"
        ]

monthdrop = OptionMenu(root, month_click, *month_options)
monthdrop.grid(column = 1, row = 1, padx=40, pady=10)

# Month Display selection
monthbutton = Button(root, text = "Show Month", command = month).grid(column = 1, row = 2, padx=40, pady=10)


# Day drop Down
def day():
    day_label = Label(root, text=day_click.get()).grid(column = 2, row = 3, padx=40, pady=10)
    global day_drop
    day_drop = day_click.get()

day_click = StringVar()
day_click.set("Select Day")

day_options = [
        "1", "2", "3", "4", "5", "6", "7", "8",
        "9", "10", "11", "12", "13", "14", "15", "16",
        "17", "18", "19", "20", "21", "22", "23", "24",
        "25", "26", "27", "28", "29", "30", "31"
        ]

daydrop = OptionMenu(root, day_click, *day_options)
daydrop.grid(column = 2, row = 1, padx=40, pady=10)

# Day Display selection
daybutton = Button(root, text = "Show Day", command = day).grid(column = 2, row = 2, padx=40, pady=10)

# Year drop Down
def year():
    year_label = Label(root, text=year_click.get()).grid(column = 3, row = 3, padx=40, pady=10)
    global year_drop
    year_drop = year_click.get()

year_click = StringVar()
year_click.set("Select Year")

year_options = [
        "2021", "2022", "2023", "2024", "2025"
        ]

yeardrop = OptionMenu(root, year_click, *year_options)
yeardrop.grid(column = 3, row = 1, padx=40, pady=10)

# Year Display selection
yearbutton = Button(root, text = "Show Year", command = year).grid(column = 3, row = 2, padx=40, pady=10)


# Hour drop Down
def hour():
    hour_label = Label(root, text=hour_click.get()).grid(column = 1, row = 6, padx=40, pady=10)
    global hour_drop
    hour_drop = hour_click.get()

hour_click = StringVar()
hour_click.set("Select Hour")

hour_options = [
        "1", "2", "3", "4", "5", "6", "7", "8",
        "9", "10", "11", "12"
        ]

hourdrop = OptionMenu(root, hour_click, *hour_options)
hourdrop.grid(column = 1, row = 4, padx=40, pady=10)

# Hour Display selection
hourbutton = Button(root, text = "Show Hour", command = hour).grid(column = 1, row = 5, padx=40, pady=10)


# Minute drop Down
def minute():
    minute_label = Label(root, text=minute_click.get()).grid(column = 2, row = 6, padx=40, pady=10)
    global minute_drop
    minute_drop = minute_click.get()

minute_click = StringVar()
minute_click.set("Select Minute")

minute_options = [
        "00", "05", "10", "15", "20", "25", "30", "35",
        "40", "45", "50", "55"
        ]

minutedrop = OptionMenu(root, minute_click, *minute_options)
minutedrop.grid(column = 2, row = 4, padx=40, pady=10)

# Minute Display selection
minutebutton = Button(root, text = "Show Minute", command = minute).grid(column = 2, row = 5, padx=40, pady=10)


# AmPM drop Down
def ampm():
    ampm_label = Label(root, text=ampm_click.get()).grid(column = 3, row = 6, padx=40, pady=10)
    global ampm_drop
    ampm_drop = ampm_click.get()

ampm_click = StringVar()
ampm_click.set("Select AM/PM")

ampm_options = [
        "AM", "PM"
        ]

ampmdrop = OptionMenu(root, ampm_click, *ampm_options)
ampmdrop.grid(column = 3, row = 4, padx=40, pady=10)

# AMPM Display selection
ampmbutton = Button(root, text = "Show AM/PM", command = ampm).grid(column = 3, row = 5, padx=40, pady=10)


#creating a checkbox for selecting the incident type
incident_list = []

def incident_selection():
	global incident_list
	for i in type_list:
		if i == 1:
			incident_list += i
	 


typeincidentlbl = Label(root, text = "Select the type of incident (select all that apply)").grid(column = 0, row = 7)

incidentvar1 = IntVar()
incidentvar2 = IntVar()
incidentvar3 = IntVar()
incidentvar4 = IntVar()
incidentvar5 = IntVar()
incidentvar6 = IntVar()
incidentvar7 = IntVar()

type_cb1 = Checkbutton(root, text = "Intellectual Property Theft", variable = incidentvar1).grid(column = 0, row = 8, sticky = W)

type_cb2 = Checkbutton(root, text = "Financial Crime", variable = incidentvar2).grid(column = 0, row = 9, sticky = W)

type_cb3 = Checkbutton(root, text = "Insider Threat", variable = incidentvar3).grid(column = 0, row = 10, sticky = W)

type_cb4 = Checkbutton(root, text = "Destructive Attacks", variable = incidentvar4).grid(column = 0, row = 11, sticky = W)

type_cb5 = Checkbutton(root, text = "Protected Health Information", variable = incidentvar5).grid(column = 0, row = 12, sticky = W)

type_cb6 = Checkbutton(root, text = "Personally Identifiable Information", variable = incidentvar6).grid(column = 0, row = 13, sticky = W)

type_cb7 = Checkbutton(root, text = "Other", variable = incidentvar7).grid(column = 0, row = 14, sticky = W)

type_list = [
	int(incidentvar1.get()),
	int(incidentvar2.get()),
	int(incidentvar3.get()),
	int(incidentvar4.get()),
	int(incidentvar5.get()),
	int(incidentvar6.get()),
	int(incidentvar7.get())
]


#making an input text field to PDF
user_in = str() 

#affect applicaitons/user accounts/networks label and input
affected = Text(root, height =3, width = 60) 
affected_label=Label(root, text="Affected Applications/User Accounts/Networks: ",font=10)
affected_label.grid(column = 1, row =7, padx=20, pady=20, sticky = E) 
affected.grid(column = 2, columnspan =2, row =7)

#malicious software/exploited vulnerabilities label and input
malicious = Text(root, height =3, width = 60) 
malicious_label=Label(root, text="Exploited Vulnerabilities: ",font=10)
malicious_label.grid(column = 1, row =8, padx=20, pady=20, sticky = E) 
malicious.grid(column = 2, columnspan =2, row =8)

#information accessed label and input
infoaccessed = Text(root, height =3, width = 60) 
infoaccessed_label=Label(root, text="Information Accessed: ",font=10)
infoaccessed_label.grid(column = 1, row =9, padx=20, pady=20, sticky = E) 
infoaccessed.grid(column = 2, columnspan =2, row =9)


#Malware Analysis label and input
malwareA = Text(root, height =3, width = 60) 
malwareA_label=Label(root, text="Malware Analysis: ",font=10)
malwareA_label.grid(column = 1, row =10, padx=20, pady=20, sticky = E) 
malwareA.grid(column = 2, columnspan =2, row =10)


#Severity of Exposure label and input
exposure = Text(root, height =3, width = 60) 
exposure_label=Label(root, text="Severity of Exposure: ",font=10)
exposure_label.grid(column = 1, row =11, padx=20, pady=20, sticky = E) 
exposure.grid(column = 2, columnspan =2, row =11)

#Major Findings label and input
majorfindings = Text(root, height =3, width = 60) 
majorfindings_label=Label(root, text="Major Findings: ",font=10)
majorfindings_label.grid(column = 1, row =12, padx=20, pady=20, sticky = E) 
majorfindings.grid(column = 2, columnspan =2, row =12)

#Containment and Eradication Activities label and input
containmentact = Text(root, height =3, width = 60) 
containmentact_label=Label(root, text="Containment and Eradication Activities: ",font=10)
containmentact_label.grid(column = 1, row =13, padx=20, pady=20, sticky = E) 
containmentact.grid(column = 2, columnspan =2, row =13)

#Strategic Recommendations label and input
strategicrec = Text(root, height =3, width = 60) 
strategicrec_label=Label(root, text="Strategic Recommendations: ",font=10)
strategicrec_label.grid(column = 1, row =14, padx=20, pady=20, sticky = E) 
strategicrec.grid(column = 2, columnspan =2, row =14)

#PDF formatting
def generatePDF():
    canvas = Canvas("user_input.pdf")
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

def submit():
     
    global user_in, root
    report_type_input = "- Report Type: " + report_type
    month_drop_input = "- Date: " + month_drop
    day_drop_input = day_drop
    year_drop_input = year_drop
    hour_drop_input = "- Time: " + hour_drop
    minute_drop_input = minute_drop
    ampm_drop_input = ampm_drop
    #incident_list_input = "- Type of Incident: " + ' '.join(incident_list)
    affected_input = "- Affected Applications/User Accounts/Networks: " + affected.get(1.0, "end-1c")
    malicious_input = "- Exploited Vulnerabilities: " + malicious.get(1.0, "end-1c")
    infoaccessed_input = "- Information Accessed: " + infoaccessed.get(1.0, "end-1c")
    exposure_input = "- Severity of Exposure: " + exposure.get(1.0, "end-1c")
    majorfindings_input = "- Major Findings: " + majorfindings.get(1.0, "end-1c")
    containmentact_input = "- Containment and Eradication Activities: " + containmentact.get(1.0, "end-1c")
    strategicrec_input = "- Strategic Recommendations: " + strategicrec.get(1.0, "end-1c")


    user_in = (report_type_input + '\n' + month_drop_input + ' ' + day_drop_input + ', ' + year_drop_input + '\n' 
+ hour_drop_input + ':' + minute_drop_input + ' ' + ampm_drop_input + '\n' + affected_input + '\n' + malicious_input
+ '\n' + infoaccessed_input + '\n' + exposure_input + '\n' + majorfindings_input
+ '\n' + containmentact_input + '\n' + strategicrec_input + '\n' )
    
    generatePDF()
 
submit_button = Button(root, text="submit", command=submit) 
submit_button.grid(column = 2, row = 21) 

#call the mainloop funtion to run the program
root.mainloop()