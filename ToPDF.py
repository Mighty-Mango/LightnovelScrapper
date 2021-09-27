from fpdf import FPDF

# need to make a input for the targeted txt file and the name of the pdf.
pdf = FPDF()
pdf.add_page()
pdf.add_font("fireflysung", '', 'fireflysung.ttf', uni=True)
pdf.set_font('fireflysung', '', 15)
f = open("Output.txt", encoding='utf-8')

for x in f:
    pdf.write(6, x)
    pdf.ln()
f.close()
pdf.output("test.pdf")

