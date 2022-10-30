from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font(family="arial", style="", size=40)
        self.cell(80)
        self.cell(30, 50, "CS50 Shirtificate", border=0, align="C")
        self.set_y(120)
        self.image("shirtificate.png", 4.5, 70, w=200)
        self.cell(80)
        x = input("Name: ") + " took CS50"
        self.set_font("helvetica", "", 25)
        self.set_text_color(255, 255, 255)
        self.cell(30, 50, txt=x, border=0, align="C")


pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
