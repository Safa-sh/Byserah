from main import *
from fpdf import FPDF
import datetime

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 18)
#  header
pdf.image("images/ImagLogo.GIF", 170, 3, 25)
pdf.cell(0, 10, "Report", border=False, ln=1, align="C")
pdf.ln()
#####General Information
pdf.set_font('Arial', 'B', 12)
pdf.set_fill_color(213, 201, 239)
pdf.cell(0, 9, 'General Information', 0, 1, 'L', 1)
pdf.ln(3)
pdf.line(8, 20,150, 20)
pdf.set_font('Arial', 'IB', 13)
pdf.cell(130, 10, txt="Paitant ID :  ",
             ln=1, align='E',)
pdf.set_font('Arial', 'B', 12)
pdf.cell(130, 10, txt="Check up No:", align="W")
pdf.cell(100, 10, txt=" Test Result Data: "+datetime.date.today().strftime("%d-%m-%y"),
             ln=1, align="E")
##Result
pdf.ln()
pdf.set_font('Arial', 'B', 12)
pdf.set_fill_color(213, 201, 239)
pdf.cell(0, 9, ' Result Infromation', 0, 1, 'L', 1)
pdf.image("images/example.jpg", 90, 100, 100)
pdf.ln()
pdf.set_font('Arial','B' , 16)
pdf.cell(0, 10, txt=" The disease is ", align="W")

# footer
pdf.set_font('Arial','' , 13)
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_y(270)
pdf.cell(0, 10, f'Page {pdf.page_no()}/nb', align="C")
pdf.alias_nb_pages(alias='nb')
# add another cell
P = testframe()
pdf.output("results/"+str(P.P_ID)+".pdf")