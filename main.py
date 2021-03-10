from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
root = Tk()

#creating label window
root.title("Basyrah")
root.iconbitmap('images/logo.ico')
####################################################
my_img = Image.open("images/ImagLogo.GIF")
resized = my_img.resize((200,200),Image.ANTIALIAS)
newsize = ImageTk.PhotoImage(resized)
labalimg = Label(image=newsize)
labalimg.pack()
labalimg.place(x = 280, y = 130)
###############################################################3
welcomLebal= Label(root,text = "WELCOME TO BASYRAH",font=('Calibri', 22))
welcomLebal.place(x = 250, y = 40)
########################################################
my_canvas = Canvas(root,width=700,height=10,bg="white")
my_canvas.create_line(0,10,700,10,fill="purple")
my_canvas.pack(pady=90)
####################################################
#Buttons
UploadImagebtn=Button(root, text="Upload Image").place(x = 150, y = 370)
DonRestn=Button(root, text="Download result").place(x = 550, y = 370)
#shoving it onto the screen
app_width = 800
app_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(width=False, height=False)
root.configure(bg='white')
root.mainloop()

