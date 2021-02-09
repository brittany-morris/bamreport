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
lbl = Label(root, text = "Welcome To Bam Reporting",font=25)
lbl.grid(column = 0, row = 2)



#making a date entry widget

select_date_lbl = Label(root, text = "Please select the date").grid(column = 2, row = 1) 

cal = Calendar(root, selectmode = "day", year = 2021, month = 2, day = 5)
cal.grid(column = 2 , row = 2)

def grab_date():
    cal_label.config(text = cal.get_date())

cal_button = Button(root, text = "Select Date", command = grab_date)
cal_button.grid(column = 3, row = 2)

cal_label = Label(root, text = "")
cal_label.grid(column = 3, row = 1)



#creating a dropdown menu
def show2():
    lbl2 = Label(root, text=clicked1.get()).grid(column = 2, row = 3)

clicked1 = StringVar()
clicked1.set("Report Type")

options1 = [
        "Incident Response Report"
        ]

drop = OptionMenu(root, clicked1, *options1)
drop.grid(column = 0, row = 4)

#displays selection
myButton = Button(root, text = "show selection", command = show2).grid(column = 0, row = 5)


#creating a checkbox for selecting the incident type

typeincidentlbl = Label(root, text = "Select the type of incident (select all that apply)").grid(column = 0, row = 7)

incidentvar1 = IntVar()
incidentvar2 = IntVar()
incidentvar3 = IntVar()
incidentvar4 = IntVar()
incidentvar5 = IntVar()
incidentvar6 = IntVar()
incidentvar7 = IntVar()

type_cb1 = Checkbutton(root, text = "Intellectual Property Theft", variable = incidentvar1, anchor = W).grid(column = 0, row = 8)

type_cb2 = Checkbutton(root, text = "Financial Crime", variable = incidentvar2, anchor = W).grid(column = 0, row = 9)

type_cb3 = Checkbutton(root, text = "Insider Threat", variable = incidentvar3, anchor = W).grid(column = 0, row = 10)

type_cb4 = Checkbutton(root, text = "Destructive Attacks", variable = incidentvar4, anchor = W).grid(column = 0, row = 11)

type_cb5 = Checkbutton(root, text = "Protected Health Information", variable = incidentvar5, anchor = W).grid(column = 0, row = 12)

type_cb6 = Checkbutton(root, text = "Personally Identifiable Information", variable = incidentvar6, anchor = W).grid(column = 0, row = 13)

type_cb7 = Checkbutton(root, text = "Other", variable = incidentvar7, anchor = W).grid(column = 0, row = 14)


#making an input text field to PDF
canvas = Canvas("user_input.pdf")
user_in = str() 

#time label and input
time = Text(root, height =1, width = 30) 
time_label=Label(root, text="Time:",font=10)
time_label.grid(column =2, row=4, padx=40, pady=10)
time.grid(column = 3, row =4)

#stakeholder label and input
stakeholders = Text(root, height =1, width = 30) 
stakeholders_label=Label(root, text="Stakeholders:",font=10)
stakeholders_label.grid(column = 2, row =5, padx=40, pady=10) 
stakeholders.grid(column = 3, row =5)

#affect applicaitons/user accounts/networks label and input
affected = Text(root, height =1, width = 30) 
affected_label=Label(root, text="Affected Applications/User Accounts/Networks: ",font=10)
affected_label.grid(column = 2, row =6, padx=40, pady=10) 
affected.grid(column = 3, row =6)

#malicious software/exploited vulnerabilities label and input
malicious = Text(root, height =1, width = 30) 
malicious_label=Label(root, text="Malicious Software / Exploited Vulnerabilities: ",font=10)
malicious_label.grid(column = 2, row =7, padx=40, pady=10) 
malicious.grid(column = 3, row =7)

#information accessed label and input
infoaccessed = Text(root, height =1, width = 30) 
infoaccessed_label=Label(root, text="Information Accessed: ",font=10)
infoaccessed_label.grid(column = 2, row =8, padx=40, pady=10) 
infoaccessed.grid(column = 3, row =8)

#Initial attack Vector label and input
attackV = Text(root, height =1, width = 30) 
attackV_label=Label(root, text="Initial attack Vector: ",font=10)
attackV_label.grid(column = 2, row =9, padx=40, pady=10) 
attackV.grid(column = 3, row =9)

#Live Response Analysis label and input
liveresponse = Text(root, height =1, width = 30) 
liveresponse_label=Label(root, text="Live Response Analysis: ",font=10)
liveresponse_label.grid(column = 2, row =10, padx=40, pady=10) 
liveresponse.grid(column = 3, row =10)

#Log Analysis label and input
loganalysis = Text(root, height =1, width = 30) 
loganalysis_label=Label(root, text="Log Analysis: ",font=10)
loganalysis_label.grid(column = 2, row =11, padx=40, pady=10) 
loganalysis.grid(column = 3, row =11)

#Malware Analysis label and input
malwareA = Text(root, height =1, width = 30) 
malwareA_label=Label(root, text="Malware Analysis: ",font=10)
malwareA_label.grid(column = 2, row =12, padx=40, pady=10) 
malwareA.grid(column = 3, row =12)

#Forensic Analysis label and input
forensicA = Text(root, height =1, width = 30) 
forensicA_label=Label(root, text="Forensic Analysis: ",font=10)
forensicA_label.grid(column = 2, row =13, padx=40, pady=10) 
forensicA.grid(column = 3, row =13)

#Severity of Exposure label and input
exposure = Text(root, height =1, width = 30) 
exposure_label=Label(root, text="Severity of Exposure: ",font=10)
exposure_label.grid(column = 2, row =14, padx=40, pady=10) 
exposure.grid(column = 3, row =14)

#Major Findings label and input
majorfindings = Text(root, height =1, width = 30) 
majorfindings_label=Label(root, text="Major Findings: ",font=10)
majorfindings_label.grid(column = 2, row =15, padx=40, pady=10) 
majorfindings.grid(column = 3, row =15)

#Containment and Eradication Activities label and input
containmentact = Text(root, height =1, width = 30) 
containmentact_label=Label(root, text="Containment and Eradication Activities: ",font=10)
containmentact_label.grid(column = 2, row =16, padx=40, pady=10) 
containmentact.grid(column = 3, row =16)

#Strategic Recommendations label and input
strategicrec = Text(root, height =1, width = 30) 
strategicrec_label=Label(root, text="Strategic Recommendations: ",font=10)
strategicrec_label.grid(column = 2, row =17, padx=40, pady=10) 
strategicrec.grid(column = 3, row =17)

def submit(): 
    global user_in, root
    time_input = "- Time: " + time.get(1.0, "end-1c")
    stakeholders_input = "- Stakeholders: " + stakeholders.get(1.0, "end-1c")
    affected_input = "- Affected Applications/User Accounts/Networks: " + affected.get(1.0, "end-1c")
    malicious_input = "- Malicious Software / Exploited Vulnerabilities: " + malicious.get(1.0, "end-1c")
    infoaccessed_input = "- Information Accessed: " + infoaccessed.get(1.0, "end-1c")
    attackV_input = "- Initial attack Vector: " + attackV.get(1.0, "end-1c")
    liveresponse_input = "- Live Response Analysis: " + liveresponse.get(1.0, "end-1c")
    loganalysis_input = "- Log Analysis: " + loganalysis.get(1.0, "end-1c")
    malwareA_input = "- Malware Analysis: " + malwareA.get(1.0, "end-1c")
    forensicA_input = "- Forensic Analysis: " + forensicA.get(1.0, "end-1c")
    exposure_input = "- Severity of Exposure: " + exposure.get(1.0, "end-1c")
    majorfindings_input = "- Major Findings: " + majorfindings.get(1.0, "end-1c")
    containmentact_input = "- Containment and Eradication Activities: " + containmentact.get(1.0, "end-1c")
    strategicrec_input = "- Strategic Recommendations: " + strategicrec.get(1.0, "end-1c")


    user_in = (time_input + '\n' + stakeholders_input + '\n' + affected_input + '\n' + malicious_input
+ '\n' + infoaccessed_input + '\n' + attackV_input + '\n' + liveresponse_input + '\n' + loganalysis_input
+ '\n' + malwareA_input + '\n' + forensicA_input + '\n' + exposure_input + '\n' + majorfindings_input
+ '\n' + containmentact_input + '\n' + strategicrec_input)
    
    root.destroy() 
 
submit_button = Button(root, text="submit", command=submit) 
submit_button.grid(column = 2, row = 21) 
root.mainloop() 

user_in_lines = user_in.split('\n') 

#PDF formatting
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