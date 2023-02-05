from tkinter import *
import datetime

def calculate_age():
    b_year = int(birth_year_entry.get())
    b_month = int(birth_month_entry.get())
    b_day = int(birth_day_entry.get())
    b_date = datetime.date(b_year,b_month,b_day)
    today = datetime.date.today()
    age = today.year - b_date.year
    txt = Text(root, width = 10)
    txt.grid(column= 0, row = 5)
    txt.insert(END, "You are {} years old!".format(age))

root = Tk()
root.title("Age Calculator")
root.geometry("450x500")
birth_year = Label(root, text="Year : ", font=("Helvetica", 10))
birth_year.grid(column = 0, row =1)
birth_month = Label(root, text = "Month: ", font = ("Helvetica", 10))
birth_month.grid(column = 0, row = 2)
birth_day = Label(root, text = "day: ", font = ("Helvetica", 10))
birth_day.grid(column = 0, row =3)
birth_year_entry = Entry(root, width = 20)
birth_year_entry.grid(column = 1, row =1)
birth_month_entry = Entry(root,width = 20)
birth_month_entry.grid(column = 1, row = 2)
birth_day_entry = Entry(root,width = 20)
birth_day_entry.grid(column = 1, row =3)
button1 = Button(root, text ="Calculate", font = ("Helvetica", 11), command = calculate_age, bg = "blue", fg = "red" )
button1.grid(column =1, row =4)
root.mainloop()
