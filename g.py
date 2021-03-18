
from tkinter import *
import tkinter.messagebox as tmsg
import sqlite3 as sq
from collections import OrderedDict
import tkinter.ttk as ttk
class  patientDB:
    def conStart(self):
        con = sq.connect("basyrah.db")
        cursor = con.cursor()
        cursor.execute("""
           CREATE TABLE IF NOT EXISTS patient (
          `patient_id` int NOT NULL ,
          `total_checkup` int DEFAULT ZEROFILL,
           PRIMARY KEY (`patient_id`)
            )
        """)
        cursor.execute("""
             CREATE TABLE IF NOT EXISTS checkup(
              checkup_id int NOT NULL ,
              `patientID` int NOT NULL,
              `checkup_result` TEXT NOT NULL,
             PRIMARY KEY (`checkup_id`),
             FOREIGN KEY (`patientID`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE)
                """)
        con.commit()
        con.close()
    def __init__(self,root,title,chooseNu):
        self.patientID_window= Toplevel(root, bg="white")
        self.patientID_window .geometry('500x500')
        self.patientID_window .title(title)
        self.View()
        self.conStar()
        self.chooseNu
        self.patientID = StringVar()


    def View(self):
       def checkSubmit():
            con = sq.connect("data.db")
            cursor = con.cursor()
            patientID = patientIDEntry.get()
            data = cursor.fetchall()
            data_imp = OrderedDict(data)
            if (patientID not in data_imp.keys()):
                self.error2()



       def on_click(event):
         patientIDEntry .configure(state=NORMAL)
         patientIDEntry .delete(0, END)
         patientIDEntry .unbind('<Button-1>', on_click_id)

       labal1 = Label(self.patientID_window, text="l", font=('Calibri', 14), bg="white")
       labal1.place(x=125, y=10)
       patientIDEntry = Entry(self.patientID_window, width=30, font=('Calibri', 12))
       patientIDEntry .insert(0, "Enter PatientID. ")
       patientIDEntry .configure(state=DISABLED)
       on_click_id = patientIDEntry.bind('<Button-1>', on_click)
       patientIDEntry .pack()
       submtbtn = Button(self.patientID_window, text="Submit", width=15, height=1, bg="white", command=checkSubmit())
       submtbtn.place(x=110, y=230)


            # =============================Putting Data

    def post(self,Id_p):

            con = sq.connect("basyrah.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM patient")
            data = cursor.fetchall()
            data_imp = OrderedDict(data)
            if (self.user.get() in data_imp.keys()):
                self.error2()
            cursor.execute("INSERT INTO patient VALUES(?,?)", (Id_p,+1))
            con.commit()
            con.close()
            self.succees2()
            # =============================Getting Data

    def get(self):
            con = sq.connect("basyrah.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM patient")
            data = cursor.fetchall()
            data_imp = OrderedDict(data)
            # ======================Condition Checked For Login
            if (self.user.get() in data_imp.keys()):
                self.succees()
            else:
                self.error()

#================================Succees Message
    def succees(self):
        a = tmsg.showinfo('Login Succeesful',"Thanks For Coming Back")
        if a == 'ok':
            self.secondScreen()

#==============================Error Message
    def error(self):
        tmsg.showerror('Error',"Username Not Found")

#====================================Second Error
    def error2(self):
        tmsg.showerror("Error","User Already Found")
#========================================Second Success
    def succees2(self):
        tmsg.showinfo("Succees","Account Create Succeesfully")




if __name__ == "__main__":
    root = Tk()
    l=patientDB(root)
    root.mainloop()