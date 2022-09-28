import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

# create main window
window = tk.Tk()
window.title("Outing & Access")
window.geometry("700x500")
# window.config(bg='pink')
bg = PhotoImage(file="C:/Users/User/Downloads/background dsp 2.png")
my_label = Label(window, image=bg)
my_label.place(relwidth=1, relheight=1)

window3 = None
window4 = None
# title , 1page
Tops = Frame(window, width=350, height=50, bd=10, relief='raise', bg='lavender blush')
Tops.pack(side=TOP)
Tops.place(relx=0.5,
           rely=0.2,
           anchor='center')
TitleLabel = tk.Label(Tops, font=('Lucida Handwriting', 30, 'bold'),
                      text="WELCOME TO SMARTRANCE", fg='white', bg='SlateBlue4')
TitleLabel.grid(row=0, column=0)

Label_Id = tk.Label(window, text='Matric ID', bg='lavender',width=100 , font=('century', 13))
Label_Id.place(relx=0.5,
               rely=0.4,
               anchor='center')

matricId = tk.StringVar()

entry_Id = tk.Entry(window, fg='black', bg='light grey', width=25, textvariable=matricId)
entry_Id.place(relx=0.5,
               rely=0.47,
               anchor='center')

window2 = None

# 2nd window,login button function
def login():
    global window2
    matricid = matricId.get()
    file = open("user.text", "w")
    file.write("matric ID:" + matricid)
    file.close()
    if (matricid == ""):
        messagebox.showinfo("", "Please key in your Matric ID.")
    else:
        messagebox.showinfo("", "LOGIN SUCCESS!")
        window2 = tk.Toplevel()
        window2.title("Student Overnight / Outing ")
        window2.geometry("700x500")
        window2.config(bg='lavender')

        checkOut_btn = tk.Button(window2, text='CHECK OUT')
        checkOut_btn.place(relx=0.5,
                           rely=0.2,
                           anchor='center')
        btncheckout = tk.Button(window2, text='CHECK OUT', command=checkout)
        btncheckout.place(relx=0.5,
                          rely=0.2,
                          anchor='center')

        checkIn_btn = tk.Button(window2, text='CHECK IN')
        checkIn_btn.place(relx=0.5,
                          rely=0.4,
                          anchor='center')
        btncheckin = tk.Button(window2, text='CHECK IN', command=checkin)
        btncheckin.place(relx=0.5,
                         rely=0.4,
                         anchor='center')

        covidlabel = tk.Label(window2, text='* If outing more than 8 hours Please do Covid-19 saliva Test',
                              bg='lavender',
                              font=('arial', 13))
        covidlabel.place(relx=0.5,
                         rely=0.6,
                         anchor='center')


loginbtn = tk.Button(window, text='LOGIN', command=login)
loginbtn.place(relx=0.5,
               rely=0.6,
               width=50,
               anchor='center')


def checkout():
    global window2, window3
    window3 = tk.Toplevel()
    window3.title("Check Out")
    window3.geometry("800x600")
    window3.config(bg='lavender')

    type_label = tk.Label(window3, text='Type :', bg='lavender', font=('arial', 12))  # type label
    type_label.place(relx=0.1,
                     rely=0.1,
                     anchor='w')
    dateFrom_label = tk.Label(window3, text='Date From :', bg='lavender', font=('arial', 12))  # date from label
    dateFrom_label.place(relx=0.1,
                         rely=0.2,
                         anchor='w')

    phoneNo_label = tk.Label(window3, text='Phone Number :', bg='lavender', font=('arial', 12))  # Phone No label
    phoneNo_label.place(relx=0.1,
                        rely=0.6,
                        anchor='w')
    PhoneNo_entry = tk.Entry(window3, fg='black', bg='light grey', width=20)
    PhoneNo_entry.place(relx=0.25,
                        rely=0.6,
                        anchor='w')
    reason_label = tk.Label(window3, text='Reason :', bg='lavender', font=('arial', 12))  # reason label
    reason_label.place(relx=0.1,
                       rely=0.7,
                       anchor='w')
    reason_entry = tk.Entry(window3, fg='black', bg='light grey', width=50)
    reason_entry.place(relx=0.25,
                       rely=0.7,
                       height=50,
                       anchor='w')
    destination_label = tk.Label(window3, text='Destination :', bg='lavender', font=('arial', 12))  # Destination label
    destination_label.place(relx=0.1,
                            rely=0.8,
                            anchor='w')
    destination_entry = tk.Entry(window3, fg='black', bg='light grey', width=50)
    destination_entry.place(relx=0.25,
                            rely=0.8,
                            height=50,
                            anchor='w')
    timefrom_label = tk.Label(window3, text='Time (24 hours) :', bg='lavender', font=('arial', 12))  # Time Out label
    timefrom_label.place(relx=0.8,
                         rely=0.2,
                         anchor='center')

    types = ('Outing', 'Overnight')
    Spinbox(window3, from_=0, to=3, values=types, bg='light grey', font=('arial', 10)).place(relx=0.25, rely=0.1,
                                                                                             anchor='w')

    # add calendar
    cal = Calendar(window3, selectmode='day', year=2020, month=5, day=22)
    cal.place(relx=0.5,
              rely=0.3,
              anchor='center')

    def grad_date():
        date.config(text="" + cal.get_date())

    # add button and label
    Button(window3, text="Get Date", command=grad_date).place(relx=0.5, rely=0.5, anchor='center')
    date = tk.Label(window3, text=" ", bg='light grey', width=6, font=('arial', 10))
    date.place(relx=0.28,
               rely=0.2,
               anchor='center')
    timefrom_entry = tk.Entry(window3, fg='black', bg='light grey', width=10)
    timefrom_entry.place(relx=0.92,
                         rely=0.2,
                         anchor='center')
    timefrom = timefrom_entry.get()
    print(f'{timefrom}')

    apply1_btn = tk.Button(window3, text='APPLY', command=lambda: (
    writeTimeDate(cal.get_date(), timefrom_entry.get()), window3.destroy(), matricId.set(""), window2.destroy(),
    tk.messagebox.showinfo(title="Success", message="Data has been saved. Thank you")))
    apply1_btn.place(relx=0.5,
                     rely=0.9,
                     anchor='center')


def writeTimeDate(date, hrs):
    date_str = f"{date} {hrs}"  # dia jadi 5/22/20 2300, sng datetime parse string
    print(date_str)
    checkout_date = datetime.strptime(date_str, '%m/%d/%y %H%M')  # datetime parse string jd datetime object
    print(checkout_date.strftime("%Y-%m-%d %H:%M"))
    f = open("student_data.txt", "a")
    f.write(
        matricId.get() + "," + checkout_date.strftime("%Y-%m-%d,%H:%M\n"))  # write student id ngan datetime dlm file
    f.close()


def checkin():
    global window4
    window4 = tk.Toplevel()
    window4.title("Check In")
    window4.geometry("600x500")
    window4.config(bg='lavender')

    date_label = tk.Label(window4, text='Date In :', bg='lavender', font=('arial', 12))  # type label
    date_label.place(relx=0.1,
                     rely=0.2,
                     anchor='w')

    # add calendar
    cal2 = Calendar(window4, selectmode='day', year=2020, month=5, day=22)
    cal2.place(relx=0.6,
               rely=0.3,
               anchor='center')

    def calendar2():
        datein.config(text="" + cal2.get_date())

    # add button and label
    Button(window4, text="Get Date", command=calendar2).place(relx=0.6, rely=0.55, anchor='center')
    datein = tk.Label(window4, text=" ", bg='light grey', width=6, font=('arial', 12))
    datein.place(relx=0.25,
                 rely=0.2,
                 anchor='w')
    timeIn_label = tk.Label(window4, text='Time (24 hours) :', bg='lavender', font=('arial', 12))  # Destination label
    timeIn_label.place(relx=0.1,
                       rely=0.65,
                       anchor='w')
    timeIn_entry = tk.Entry(window4, fg='black', bg='light grey', width=13)
    timeIn_entry.place(relx=0.32,
                       rely=0.65,
                       anchor='w')

    apply2_btn = tk.Button(window4, text='APPLY', command=lambda: checkTimeDate(cal2.get_date(),timeIn_entry.get()))  # aku pakai lambda nk pass argument, google la anonymous function, button apply checkin
    apply2_btn.place(relx=0.5,
                     rely=0.75,
                     anchor='center')


def checkTimeDate(date, hrs):
    date_str = f"{date} {hrs}"  # dia jadi 5/22/20 2300, sng datetime parse string
    print(date_str)
    checkin_date = datetime.strptime(date_str, '%m/%d/%y %H%M')  # datetime parse string jd datetime object

    f1 = open("student_data.txt", "r")  # ni bukak as read mode sbb nk read je
    Lines = f1.readlines()  #
    f1.close()  # tutup file

    datalist = []  # Convert smua data dlm text file jd list
    match_index = 0
    count = 0
    for line in Lines:
        line = line.rstrip("\n")  # remove trailing newline
        datalist.append(line.split(","))  # tambah line by line
        count += 1
        if matricId.get() == line[0]:
            match_index = count
            break

    del Lines[match_index]  # delete yg match dlm file td

    f2 = open("student_data.txt", "w")  # ni bukak as write mode sbb nk write
    for line in Lines:  # tulis data yg dah di edit
        f2.write(line)
    f2.close()

    for col in datalist:  # pstu iterate list
        if matricId.get() == col[0]:  # col[0] matric id, col[1] tarikh, col[2] jam
            date_str = f"{col[1]} {col[2]}"  # convert jd single string untuk sng parse
            checkout_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")  # datetime parse string jd datetime object
            break

    diff_hrs = (
                           checkin_date - checkout_date).total_seconds() / 3600  # cari difference between date checkout ngan checkin, tukar jadi seconds, pstu bahagi 3600 untuk dptkan hours
    print(diff_hrs)
    if diff_hrs >= 8:  # ni ikut la lebih dari 8 jam ke 9 jam ke
        new_window()
    else:
        messagebox.showinfo("", "Check In Success")


def new_window():  # new window
    global window3, window4
    window5 = tk.Toplevel()
    window5.transient(window)
    global img
    window5.title("Exceed 8 hours")
    window5.geometry("600x700")
    window5.config(bg='lavender')

    covidlabel = tk.Label(window5,
                          text='You have outing more than 8 hours. Please do Covid-19 Saliva Test\n'
                               ' Please upload your Covid-19 Saliva Test in JPEG OR PNG files ',
                          bg='lavender',
                          font=('arial', 13))
    covidlabel.place(relx=0.5,
                     rely=0.1,
                     anchor='n')
    Label_Result = tk.Label(window5, text='Result : ', bg='lavender', font=('arial', 13))
    Label_Result.place(relx=0.1,
                       rely=0.2,
                       anchor='w')

    global result
    entry_result = tk.Entry(window5, fg='black', bg='light grey', width=20)
    entry_result.place(relx=0.25, rely=0.2, anchor='w')
    result = tk.StringVar()

    def submit():
        result = entry_result.get()
        if (result == ""):
            messagebox.showinfo("", "Please key in your Covid-19 Saliva Test Result.")
        elif (result == "Negative") or (result == "negative"):
            messagebox.showinfo("", "PLEASE SUMBIT PROOF FOR COVID-19 SALIVA TEST RESULT")
        elif (result == "Positive") or (result == "positive"):
            messagebox.showinfo("", "PLEASE CONTACT PKU IMMEDIATELY\n09-5493111.\n AND SUMBIT PROOF FOR COVID-19 SALIVA TEST RESULT")
        else:
            messagebox.showinfo("", "Invalid input")

    SubmitButton = Button(window5, text="Submit", width=7, height=1, command=submit)
    SubmitButton.place(relx=0.6, rely=0.2, anchor='center')

    DoneButton = Button(window5, text="Done", width=7, height=1, command=lambda: (
    window5.destroy(), matricId.set(""), window2.destroy(), window3.destroy(), window4.destroy(),
    tk.messagebox.showinfo(title="Success", message="Sekian terima kasih.\n~Fadcem")))
    DoneButton.place(relx=0.5, rely=0.95, anchor='center')

    def upload_file():
        f_types = [('Jpeg Files', '*.jpeg'), ('PNG Files', '*.png')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = Image.open(filename)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(window5)
        e1.place(relx=0.5, rely=0.6, anchor='center')
        e1.image = img
        e1['image'] = img

    uploadImage_button = tk.Button(window5, text="Upload Image", width=15, height=1, command=lambda: upload_file())
    uploadImage_button.place(relx=0.5, rely=0.3, anchor='center')

window.mainloop()

