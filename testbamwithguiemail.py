#!/usr/bin/env python3

from tkinter import *
from tkcalendar import * 
from textwrap import TextWrapper 
from reportlab.pdfgen.canvas import Canvas 
import smtplib, email, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#create a blank window called root
root = Tk()
root.title('Bam Reporting')
root.configure(background='#4C5F71')

#set the size
root.geometry('1250x900')

#create a label widget
#put it on a grid to determine where the label lies on the window
lbl = Label(root, text = "Welcome To Bam Reporting",font=25, background='#4C5F71', fg = "white")
lbl.grid(column = 0, row = 0)


#Report Type drop Down
def reporttype():
    reporttype_label = Label(root, text=reporttype_click.get(), background='#4C5F71', fg = "white").grid(column = 0, row =3, padx=40, pady=10 )
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
reporttypebutton = Button(root, text = "show selection", command = reporttype, background='#4C5F71', fg = "white").grid(column = 0, row = 2, padx=40, pady=10)


# Month drop Down
def month():
    month_label = Label(root, text=month_click.get(), background='#4C5F71', fg = "white").grid(column = 1, row = 3, padx=40, pady=10)
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
monthbutton = Button(root, text = "Show Month", command = month, background='#4C5F71', fg = "white").grid(column = 1, row = 2, padx=40, pady=10)


# Day drop Down
def day():
    day_label = Label(root, text=day_click.get(), background='#4C5F71', fg = "white").grid(column = 2, row = 3, padx=40, pady=10)
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
daybutton = Button(root, text = "Show Day", command = day, background='#4C5F71', fg = "white").grid(column = 2, row = 2, padx=40, pady=10)

# Year drop Down
def year():
    year_label = Label(root, text=year_click.get(), background='#4C5F71', fg = "white").grid(column = 3, row = 3, padx=40, pady=10)
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
yearbutton = Button(root, text = "Show Year", command = year, background='#4C5F71', fg = "white").grid(column = 3, row = 2, padx=40, pady=10)



address = StringVar()
email_body = StringVar()
#email function
def destroy_window():
    root.destroy()

def send_message():
    address_info = address_entry.get()
    email_body_info = email_body_entry.get()
    #print(address_info,email_body_info)
    sender_email = "bamreport302@gmail.com"
    sender_password = "Fullstack2011"   
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)
    print("Login successful")
#    server.sendmail(sender_email,address_info,email_body_info)
    print("Message sent")
# Create a multipart message and set headers
    message = MIMEMultipart()
# Add body to email
    message.attach(MIMEText(email_body_info, "plain"))
    filename = "user_input.pdf"  # In same directory as script with your .pdf file
# Open PDF file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
# Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
# Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
)
# Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
# Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, address_info, text)
	
email_button = Button(root, text="email", command=destroy_window, background='#4C5F71', fg = "white") 
email_button.grid(column = 3, row = 21)

#creating a checkbox for selecting the incident type

incident_list = []
count = 0
def incident_selection():
        global count
        global incident_list
        type_list = [
        int(incidentvar1.get()),
        int(incidentvar2.get()),
        int(incidentvar3.get()),
        int(incidentvar4.get()),
        int(incidentvar5.get()),
        int(incidentvar6.get()),
        int(incidentvar7.get())
        ]
        for i in type_list:
                if i == 1:
                        incident_list += inc_strings[type_list.index(i, count)]
                        incident_list += ', '
                count += 1
        del incident_list[-2]
        return incident_list
inc_strings = [
        "Intellectual Property Theft",
        "Financial Crime",
        "Insider Threat",
        "Destructive Attacks",
        "Protected Health Information",
        "Personally Identifiable Information",
        "Other"
]

typeincidentlbl = Label(root, text = "Type of incident (select all that apply)", background='#4C5F71', fg = "white").grid(column = 0, row = 7)

incidentvar1 = IntVar()
incidentvar2 = IntVar()
incidentvar3 = IntVar()
incidentvar4 = IntVar()
incidentvar5 = IntVar()
incidentvar6 = IntVar()
incidentvar7 = IntVar()

type_cb1 = Checkbutton(root, text = "Intellectual Property Theft", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar1).grid(column = 0, row = 8, sticky = W)

type_cb2 = Checkbutton(root, text = "Financial Crime", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar2).grid(column = 0, row = 9, sticky = W)

type_cb3 = Checkbutton(root, text = "Insider Threat", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar3).grid(column = 0, row = 10, sticky = W)

type_cb4 = Checkbutton(root, text = "Destructive Attacks", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar4).grid(column = 0, row = 11, sticky = W)

type_cb5 = Checkbutton(root, text = "Protected Health Information", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar5).grid(column = 0, row = 12, sticky = W)

type_cb6 = Checkbutton(root, text = "Personally Identifiable Information", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar6).grid(column = 0, row = 13, sticky = W)

type_cb7 = Checkbutton(root, text = "Other", bg='#4C5F71', fg = "white", activebackground = '#4C5F71', activeforeground = 'white', selectcolor = '#4C5F71', variable = incidentvar7).grid(column = 0, row = 14, sticky = W)



#making an input text field to PDF
user_in = str() 

#time label and input
time = Text(root, height =1, width = 60) 
time_label=Label(root, text="Time of Incident: ", background='#4C5F71', fg = "white")
time_label.grid(column = 1, row =6, padx=20, pady=20, sticky = E,) 
time.grid(column = 2, columnspan =2, row =6)

#affect applicaitons/user accounts/networks label and input
affected = Text(root, height =3, width = 60) 
affected_label=Label(root, text="Affected Applications/User Accounts/Networks: ", background='#4C5F71', fg = "white")
affected_label.grid(column = 1, row =7, padx=20, pady=20, sticky = E) 
affected.grid(column = 2, columnspan =2, row =7)

#malicious software/exploited vulnerabilities label and input
malicious = Text(root, height =3, width = 60) 
malicious_label=Label(root, text="Exploited Vulnerabilities: ", background='#4C5F71', fg = "white")
malicious_label.grid(column = 1, row =8, padx=20, pady=20, sticky = E) 
malicious.grid(column = 2, columnspan =2, row =8)

#information accessed label and input
infoaccessed = Text(root, height =3, width = 60) 
infoaccessed_label=Label(root, text="Information Accessed: ", background='#4C5F71', fg = "white")
infoaccessed_label.grid(column = 1, row =9, padx=20, pady=20, sticky = E) 
infoaccessed.grid(column = 2, columnspan =2, row =9)


#Malware Analysis label and input
malwareA = Text(root, height =3, width = 60) 
malwareA_label=Label(root, text="Malware Analysis: ", background='#4C5F71', fg = "white")
malwareA_label.grid(column = 1, row =10, padx=20, pady=20, sticky = E) 
malwareA.grid(column = 2, columnspan =2, row =10)


#Severity of Exposure label and input
exposure = Text(root, height =3, width = 60) 
exposure_label=Label(root, text="Severity of Exposure: ", background='#4C5F71', fg = "white")
exposure_label.grid(column = 1, row =11, padx=20, pady=20, sticky = E) 
exposure.grid(column = 2, columnspan =2, row =11)

#Major Findings label and input
majorfindings = Text(root, height =3, width = 60) 
majorfindings_label=Label(root, text="Major Findings: ", background='#4C5F71', fg = "white")
majorfindings_label.grid(column = 1, row =12, padx=20, pady=20, sticky = E) 
majorfindings.grid(column = 2, columnspan =2, row =12)

#Containment and Eradication Activities label and input
containmentact = Text(root, height =3, width = 60) 
containmentact_label=Label(root, text="Containment and Eradication Activities: ", background='#4C5F71', fg = "white")
containmentact_label.grid(column = 1, row =13, padx=20, pady=20, sticky = E) 
containmentact.grid(column = 2, columnspan =2, row =13)

#Strategic Recommendations label and input
strategicrec = Text(root, height =3, width = 60) 
strategicrec_label=Label(root, text="Strategic Recommendations: ", background='#4C5F71', fg = "white")
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
    incident_selection() 
    global user_in, root
    report_type_input = "- Report Type: " + '\n' + '     - ' + report_type
    month_drop_input = "- Date: " + month_drop
    day_drop_input = day_drop
    year_drop_input = year_drop
    time_input = "- Time of Incident: " + '\n' + '     - ' + time.get(1.0, "end-1c")
    incident_list_input = "- Type of Incident: " + '\n' "     - "+ "".join(incident_list)
    affected_input = "- Affected Applications/User Accounts/Networks: "  + '\n' + '     - '+ affected.get(1.0, "end-1c")
    malicious_input = "- Exploited Vulnerabilities: "  + '\n' + '     - '+ malicious.get(1.0, "end-1c")
    infoaccessed_input = "- Information Accessed: " + '\n' + '     - ' + infoaccessed.get(1.0, "end-1c")
    exposure_input = "- Severity of Exposure: "  + '\n' + '     - '+ exposure.get(1.0, "end-1c")
    majorfindings_input = "- Major Findings: "  + '\n' + '     - '+ majorfindings.get(1.0, "end-1c")
    containmentact_input = "- Containment and Eradication Activities: "  + '\n' + '     - '+ containmentact.get(1.0, "end-1c")
    strategicrec_input = "- Strategic Recommendations: " + '\n' + '     - ' + strategicrec.get(1.0, "end-1c")


    user_in = (report_type_input +  '\n' + month_drop_input + ' ' + day_drop_input + ', ' + year_drop_input + '\n'
+ time_input + '\n' + incident_list_input + '\n' + affected_input + '\n' + malicious_input + '\n' + infoaccessed_input + '\n' 
+ exposure_input + '\n' + majorfindings_input + '\n' + containmentact_input + '\n' + strategicrec_input + '\n' )
    
    generatePDF()
 
submit_button = Button(root, text="submit", command=submit, background='#4C5F71', fg = "white") 
submit_button.grid(column = 2, row = 21) 


#call the mainloop funtion to run the program
root.mainloop()

app = Tk()
app.configure(background='#4C5F71')
app.geometry("500x500")
app.title("E-mail the PDF")
heading = Label(text="E-mail the PDF",bg="#4C5F71",fg="white",font="10",width="500",height="3")
heading.pack()
address_field = Label(text="Recipient Address :", background='#4C5F71', fg = "white")
email_body_field = Label(text="Message :", background='#4C5F71', fg = "white")
address_field.place(x=15,y=70)
email_body_field.place(x=15,y=140)
address_entry = Entry(textvariable=address,width="30")
email_body_entry = Entry(textvariable=email_body,width="30")
address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)
button = Button(app,text="Send Message",command=send_message,width="30",height="2",bg="#4C5F71", fg="white")
button.place(x=15,y=220)


mainloop()