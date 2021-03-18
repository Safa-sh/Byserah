from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox as tmsg
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

def patientID_wind(titl):
    def checkSubmit():
        patientID.get()

    def on_click(event):
     patientID.configure(state=NORMAL)
     patientID.delete(0, END)
     patientID.unbind('<Button-1>', on_click_id)

    patientID_window = Toplevel(root, bg="white")
    patientID_window.title(titl)
    labal1 = Label(patientID_window, text=titl, font=('Calibri', 14), bg="white")
    labal1.place(x=125, y=10)
    designTem(patientID_window, 350, 300)
    patientID=Entry(patientID_window,width=30,font=('Calibri', 12))
    patientID.insert(0, "Ente PatientID. ")
    patientID.configure(state=DISABLED)
    on_click_id = patientID.bind('<Button-1>', on_click)
    patientID.pack()
    submtbtn = Button(patientID_window, text="Submit", width=15, height=1, bg="white",command=checkSubmit())
    submtbtn.place(x=110, y=230)

def donResbtnFunction():
 root.filename = filedialog.askopenfilename(initialdir="C: \Interfaces\images",
             title="Select a result", filetype=    (("pdf files", "*.pdf"), ("all files", "*.*")))

def  uploadImagebtnFunction():
    choose_window = Toplevel(root, bg='white')
    designTem(choose_window,350,350)
    welcomLebal = Label(choose_window, text="WELCOME TO BASYRAH", font=('Calibri', 14), bg="white")
    welcomLebal.place(x=80, y=10)
    def click():
        if(option.get()==1):
            patientID_wind("New patient ")

        else:
            patientID_wind("Previous patient")
      # checkID(ID)
    Label(choose_window,text="Are you :", font=('Calibri', 12),bg="white",justify="right").pack()
    option = IntVar()
    Radiobutton(choose_window,text="New patient",fg="purple" ,bg="white",font=('Calibri', 14),variable=option,value=1).pack()
    Radiobutton(choose_window, text="Previous patient.",fg="purple" ,bg="white",font=('Calibri', 14), variable=option, value=2).pack()
    submtbtn = Button(choose_window,text="Submit",width=15,height=1,bg="white",command=click)
    submtbtn.place(x=110, y=230)
    ##root.filename = filedialog.askopenfilename(initialdir="\Interfaces\images",
                                ##               title="Select an image", filetype=
                                     ##    (("png files", "*.png"), ("all files", "*.*")))




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
    Button(root, text="Upload Image",width=20,height=2,command=uploadImagebtnFunction,bg="white").place(x=90, y=450)
    Button(root, text="Download result",width=20,height=2,command=donResbtnFunction,bg="white").place(x=550, y=450)
    root.mainloop()


if __name__ == '__main__':
    main()





