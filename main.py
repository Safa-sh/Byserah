from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
def  uploadImagebtnFunction():
    new_window=Toplevel(root)
    app_width = 350
    app_height = 300
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    new_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    new_window.resizable(width=False, height=False)
    new_window.configure(bg='white')
    new_window.title("chosse ")
    new_window.iconbitmap('images/logo.ico')
    welcomLebal = Label(new_window, text="WELCOME TO BASYRAH", font=('Calibri', 14), bg="white")
    welcomLebal.place(x=80, y=10)
    # line drawn
    my_canvas = Canvas(new_window, width=300, height=10, bg="white")
    my_canvas.create_line(0, 10, 300, 10, fill="purple")
    my_canvas.pack(pady=50)
    option=IntVar()
    option.get()
    Radiobutton(new_window,text="New patient",font=('Calibri', 14),variable=option,value=1).pack()
    Radiobutton(new_window, text="Previous patient.", font=('Calibri', 14), variable=option, value=2).pack()
    submitbtn=Button(new_window,text="Submit",width=15,height=1,bg="white").pack()
    submitbtn.place(x=150, y=150)
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
    UploadImagebtn = Button(root, text="Upload Image",width=20,height=2,command=uploadImagebtnFunction,bg="white").place(x=90, y=450)
    DonResbtn = Button(root, text="Download result",width=20,height=2,command=donResbtnFunction bg="white").place(x=550, y=450)
    root.mainloop()


if __name__ == '__main__':
    main()





