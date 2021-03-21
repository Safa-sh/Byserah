from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox as tmsg
import mysql.connector as mysql
import webbrowser as wb
root = Tk()
def designTem(Tk,app_width,app_height):
    screen_width = Tk.winfo_screenwidth()
    screen_height = Tk.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    Tk.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    Tk.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    Tk.resizable(width=False, height=False)
    Tk.iconbitmap('images/logo.ico')
    # line drawn
    my_canvas = Canvas(Tk, width=300, height=10, bg="white")
    my_canvas.create_line(0, 10, 300, 10, fill="purple")
    my_canvas.pack(pady=50)
class testframe:
    def startCon(self):
         con = mysql.connect(
            host="localhost",
            port="3308",
            user="root",
            passwd="8977749",
            database="basyrahpg")

         return con
    def __init__(self,root,type_p,P_ID):
        self.patientTest_window= Toplevel(root, bg="white")
        self.patientTest_window .geometry('500x500')
        self.patientTest_window .title("patientTest_window")
        self.P_ID= StringVar()
        self.type_p=type_p
        self.View()

    def View(self):
        designTem(self.patientTest_window, 300, 300)
        NewTestbtn = Button(self.patientTest_window, text="new test ", width=17,height=2, bg="white",fg="purple")
        NewTestbtn.place(x=90, y=90)
        showPreResbtn = Button(self.patientTest_window, text="show previous result", width=17,height=2, bg="white",fg="purple")
        showPreResbtn.place(x=90, y=160)
        if (self.type_p == 1):
            showPreResbtn.configure(state=DISABLED)
        else:
             showPreResbtn.configure(state=NORMAL)

class  patientDB:
    def startCon(self):
        con = mysql.connect(
              host="localhost",
              port="3308",
              user="root",
              passwd="8977749",
              database="basyrahpg")
        return con
    def __init__(self,root,title,chooseNu):
        self.patientID_window= Toplevel(root, bg="white")
        self.patientID_window .title(title)
        labal1 = Label(self.patientID_window, text=title, font=('Calibri', 14), bg="white")
        labal1.place(x=90, y=5)
        self.P_ID= StringVar()
        self.chooseNu=chooseNu
        self.View()
    def View(self):
      designTem(self.patientID_window, 300, 300)
      def on_click(event):
         patientIDEntry .configure(state=NORMAL)
         patientIDEntry .delete(0, END)
         patientIDEntry .unbind('<Button-1>', on_click_id)

      patientIDEntry = Entry(self.patientID_window, width=30, font=('Calibri', 12),textvariable = self.P_ID)
      patientIDEntry .insert(0, "Enter PatientID. ")
      patientIDEntry .configure(state=DISABLED)
      on_click_id = patientIDEntry.bind('<Button-1>', on_click)
      patientIDEntry.pack()
      submtbtn = Button(self.patientID_window, text="Submit", width=15, height=1, bg="white",command=self.find_patientID)
      submtbtn.place(x=110, y=230)
    #=============================find_patientID
    def find_patientID(self):
        con=self.startCon()
        Id_p=self.P_ID.get()
        if(Id_p==""):
            tmsg.showinfo('insert', "Please Enter patient_id")
        else:
               cursor = con.cursor()
               cursor.execute("SELECT patient_id FROM patient WHERE patient_id='"+Id_p+"'")
               result = cursor.fetchall()
               print(self.P_ID.get())
               if result and (self.chooseNu == 1):#new patient
                       tmsg.showerror("Error","Data Already Found")
               elif not result and(self.chooseNu == 1):
                   self.add_New_patient(Id_p)
                   testframe(root, 1,Id_p)
               elif result and (self.chooseNu == 2):#previous patient
                      testframe(root,2,Id_p)
               elif not result and(self.chooseNu == 2):#previous patient
                  a=tmsg.askquestion("","do you add it as new patiant ?")
                  if a=='yes':
                      self.add_New_patient()
        con.close()

    def add_New_patient(self,Id_p):
       #try:
        con = self.startCon()
        cursor = con.cursor()
        inserSQL="""INSERT INTO patient(patient_id,total_checkup) VALUES (%s,%s)"""
        initlv=0
        data=(Id_p,str(initlv))
        res=cursor.execute(inserSQL,data)
        if res:
            print("donnne ")
        #except EXCEPTION as err:
        con.commit()
        con.close()

def  uploadImagebtnFunction():
    choose_window = Toplevel(root, bg='white')
    designTem(choose_window,350,350)
    welcomLebal = Label(choose_window, text="WELCOME TO BASYRAH", font=('Calibri', 14), bg="white")
    welcomLebal.place(x=80, y=10)
    def click():
        if(option.get()==1):
            choose_window.destroy()
            patientDB(root,"New patient",1)

        else:
          choose_window.destroy()
          patientDB(root,"Previous patient",2)

      # checkID(ID)
    Label(choose_window,text="Are you :", font=('Calibri', 12),bg="white",justify="right").pack()
    option = IntVar()
    Radiobutton(choose_window,text="New patient",fg="purple" ,bg="white",font=('Calibri', 14),variable=option,value=1).pack()
    Radiobutton(choose_window, text="Previous patient.",fg="purple" ,bg="white",font=('Calibri', 14), variable=option, value=2).pack()
    submtbtn = Button(choose_window,text="Submit",width=15,height=1,bg="white",command=click)
    submtbtn.place(x=110, y=230)
def main():
    # Main window
    app_width = 800
    app_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    root.resizable(width=False, height=False)
    root.configure(bg='white')
    # creating label main  window
    root.title("Basyrah")
    root.iconbitmap('images/logo.ico')
    #Middle image
    my_img = Image.open("images/ImagLogo.GIF")
    resized = my_img.resize((300, 300), Image.ANTIALIAS)
    newsize = ImageTk.PhotoImage(resized)
    labalimg = Label(image=newsize,bg="white")
    labalimg.pack()
    labalimg.place(x=230, y=130)
    #Welcome Label
    welcomLebal = Label(root, text="WELCOME TO BASYRAH", font=('Calibri', 22),bg="white")
    welcomLebal.place(x=250, y=40)
    # line drawn
    my_canvas = Canvas(root, width=700, height=10, bg="white")
    my_canvas.create_line(0, 10, 700, 10, fill="purple")
    my_canvas.pack(pady=90)
    # Buttons
    def donResbtnFunction():
        root.filename = filedialog.askopenfilename(initialdir="C: \Interfaces\images",
                                                   title="Select a result",
                                                   filetype=(("pdf files", "*.pdf"), ("all files", "*.*")))
    Button(root, text="Upload Image",font=('Calibri', 12),width=20,height=2,command=uploadImagebtnFunction,bg="white").place(x=70, y=450)
    Button(root, text="Download result",font=('Calibri', 12),width=20,height=2,command=donResbtnFunction,bg="white").place(x=550, y=450)
    root.mainloop()

if __name__ == '__main__':
    main()





