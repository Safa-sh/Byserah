from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox as tmsg
import mysql.connector as mysql
from fpdf import FPDF
import time
import datetime


root = Tk()


root.filename = filedialog.askopenfilename(initialdir="results",
                                                                  title="Select a result",
                                                                  filetype=(
                                                                  ("png files", "*.png"), ("all files", "*.*")))
# Label(root,text=root.filename).pack()
# previewImageL = ImageTk.PhotoImage(Image.open(root.filename))
lan=Label(root, image=previewImageL).pack()
previewImagbtn = Button(root, text = "preview Image", width = 17, height = 2, bg = "white",
                                                                                    fg = "purple")
root.mainloop()