from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox as tmsg
import mysql.connector as mysql
from fpdf import FPDF

import datetime
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
        self.imagePa=""
        self.type_p=type_p
        self.View()

    def View(self):
        designTem(self.patientTest_window, 300, 300)
        NewTestbtn = Button(self.patientTest_window, text="new test ", width=17,height=2, bg="white",fg="purple",command=self.TestSelect)
        NewTestbtn.place(x=90, y=90)
        showPreResbtn = Button(self.patientTest_window, text="show previous result", width=17,height=2, bg="white",fg="purple")
        showPreResbtn.place(x=90, y=160)
        if (self.type_p == 1):
            showPreResbtn.configure(state=DISABLED)
        else:
             showPreResbtn.configure(state=NORMAL)

    def TestSelect(self):
        previewImageWin = Toplevel(bg="white")
        app_width = 600
        app_height = 500
        screen_width = previewImageWin.winfo_screenwidth()
        screen_height = previewImageWin.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        previewImageWin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        previewImageWin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        previewImageWin.resizable(width=False, height=False)
        previewImageWin.iconbitmap('images/logo.ico')
        def get_image():
            previewImageWin.filename = filedialog.askopenfilename(initialdir="results",
                                                                  title="Select a result",
                                                                  filetype=(
                                                                      ("png files", "*.png"), ("all files", "*.*")))
            self.imagePa = previewImageWin.filename
            previewImageL = Image.open(previewImageWin.filename)
           #get image
            resized = previewImageL.resize((400, 400), Image.ANTIALIAS)
            newsize = ImageTk.PhotoImage(resized)
            lbl.config(image=newsize)
            lbl.image=newsize

        lbl=Label(previewImageWin,text="Enter preview Image ",pady= 200,padx = 230,bd=2,relief='groove')
        lbl.pack()
        # lbl.place(x=200, y=100)
        previewImagbtn = Button(previewImageWin, text = "Preview Image", font=('Abadi', 11),width = 12, height = 1, bg = "white",  fg = "purple",command=get_image)
        previewImagbtn.place(x=300,y=450)
        Testbtn = Button(previewImageWin, text="Test ",font=('Abadi', 11), width=12, height=1, bg="white", fg="purple")#call Test
        Testbtn.place(x=150, y=450)

    # def Test(self):
    def createPDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 18)
        # header
        pdf.image("images/ImagLogo.GIF", 170, 3, 25)
        pdf.cell(0, 10, "Report", border=False, ln=1, align="C")
        pdf.ln()
        #####General Information
        pdf.set_font('Arial', 'B', 12)
        pdf.set_fill_color(213, 201, 239)
        pdf.cell(0, 9, 'General Information', 0, 1, 'L', 1)
        pdf.ln(3)
        pdf.line(8, 20, 150, 20)
        pdf.set_font('Arial', 'IB', 13)
        pdf.cell(130, 10, txt="Paitant ID :  ",
                 ln=1, align='E', )
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(130, 10, txt="Check up No:", align="W")
        pdf.cell(100, 10, txt=" Test Result Data: " + datetime.date.today().strftime("%d-%m-%y"),
                 ln=1, align="E")
        ##Result
        pdf.ln()
        pdf.set_font('Arial', 'B', 12)
        pdf.set_fill_color(213, 201, 239)
        pdf.cell(0, 9, ' Result Infromation', 0, 1, 'L', 1)
        pdf.image(self.imagePa, 90, 100, 100)
        pdf.ln()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, txt=" The disease is ", align="W")

        # footer
        pdf.set_font('Arial', '', 13)
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_y(270)
        pdf.cell(0, 10, f'Page {pdf.page_no()}/nb', align="C")
        pdf.alias_nb_pages(alias='nb')
        # add another cell
        pdf.output("results/" + self.P_ID + ".pdf")
class  patientDB:
    def startCon(self):
        con = mysql.connect(
              host="localhost",
              port="3308",
              user="root",
              passwd="8977749",
              database="basyrahpg")
        return con
    def __init__(self,choose_window,title,chooseNu):
        self.patientID_window= Toplevel(choose_window, bg="white")
        self.patientID_window .title(title)
        labal1 = Label(self.patientID_window, text=title, font=('Calibri', 14), bg="white")
        labal1.place(x=91, y=5)
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
      submtbtn.place(x=95, y=230)
    #=============================find_patientID
    def find_patientID(self):
        con=self.startCon()
        Id_p=self.P_ID.get()
        if(len(Id_p)==0):
            tmsg.showinfo('insert', "Please Enter patient_id",parent=self.patientID_window)
        else:
               cursor = con.cursor()
               cursor.execute("SELECT patient_id FROM patient WHERE patient_id='"+Id_p+"'")
               result = cursor.fetchall()
               if result and (self.chooseNu == 1):#new patient
                tmsg.showerror("Error","Data Already Found",parent=self.patientID_window)
               elif not result and(self.chooseNu == 1):
                   self.add_New_patient(Id_p)
                   testframe(root, 1,Id_p)
               elif result and (self.chooseNu == 2):#previous patient
                      testframe(root,2,Id_p)
               elif not result and(self.chooseNu == 2):#previous patient
                  a=tmsg.askquestion("","do you add it as new patiant ?",parent=self.patientID_window)
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

            patientDB(choose_window,"New patient",1)

        else:

          patientDB(choose_window,"Previous patient",2)

      # checkID(ID)
    Label(choose_window,text="Are you :", font=('Calibri', 13),bg="white").place(x=50,y=80)
    option = IntVar()
    Radiobutton(choose_window,text="New patient",fg="purple" ,bg="white",font=('Calibri', 14),variable=option,value=1).place(x=110, y=120)
    Radiobutton(choose_window, text="Previous patient.",fg="purple" ,bg="white",font=('Calibri', 14), variable=option, value=2).place(x=110, y=160)
    submtbtn = Button(choose_window,text="Submit",font=('Calibri', 11),width=15,height=1,bg="white",command=click)
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
        root.filename = filedialog.askopenfilename(initialdir="results",
                                                   title="Select a result",
                                                   filetype=(("pdf files", "*.pdf"), ("all files", "*.*")))

    Button(root, text="Upload Image",font=('Calibri', 12),width=20,height=2,command=uploadImagebtnFunction,bg="white").place(x=70, y=450)
    Button(root, text="Download result",font=('Calibri', 12),width=20,height=2,command=donResbtnFunction,bg="white").place(x=550, y=450)
    root.mainloop()
if __name__ == '__main__':
    main()









