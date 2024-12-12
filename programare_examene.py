from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def genereaza_programare_examene_pdf(exams, output_file):

    #crearea documentului PDF
    pdf=SimpleDocTemplate(output_file, pagesize=landscape(letter))

    #Titluri pentru tabel
    data=[["Materie", "Data", "Ora", "Sala","Grupa","Profesor", "Asistent"]]

    #adaugam examenele in tabel

    for exam in exams:
        data.append([exam["materie"], exam["data"], exam["ora"], exam["sala"], exam["grupa"], exam["profesor"], exam["asistent"]])

    #design-ul tabelului

    table=Table(data)
    style=TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    #adaugam tabelul in pdf
    pdf.build([table])

#exemplu de utilizare
if __name__=="__main__":
    #lista de examene
    examene=[
        {"materie": "IP", "data": "22.01.2025", "ora": "9:00", "sala": "C202", "grupa": "3142", "profesor": "Turcu Cristina", "asistent": "Petrovici Marius"},
        {"materie": "SI", "data": "25.01.2025", "ora": "12:00", "sala": "C204", "grupa": "3143", "profesor": "Turcu Corneliu", "asistent": "Gherman Ovidiu"},
        {"materie": "CMo", "data": "17.01.2025", "ora": "10:00", "sala": "C202", "grupa": "3141", "profesor": "Gherman Ovidiu", "asistent": "Tudor Alexandru"},
        {"materie": "DEEA1", "data": "27.01.2025", "ora": "9:00", "sala": "Amf.DH", "grupa": "3123", "profesor": "Graur Adrian", "asistent": "Pohoata Sorin"},
        {"materie": "SDA", "data": "02.02.2025", "ora": "11:00", "sala": "C203", "grupa": "3134", "profesor": "Pentiuc Stefan", "asistent": "Tudor Alexandru"},
        {"materie": "PCLP1", "data": "03.02.2025", "ora": "14:00", "sala": "C303", "grupa": "3112", "profesor": "Prodan Remus", "asistent": "Siean Alexandru"},
        {"materie": "PBD", "data": "04.02.2025", "ora": "11:00", "sala": "C209", "grupa": "3141", "profesor": "Danubianu Mirela", "asistent": "Barila Adina"},
        {"materie": "RC", "data": "06.02.2025", "ora": "9:00", "sala": "Amf.RR", "grupa": "3122", "profesor": "Potoran Alin", "asistent": "Beguni Catalin"},
    ]
    #generam pdf-ul
    genereaza_programare_examene_pdf(examene,"program_examene.pdf")
    print("PDF-ul a fost creat cu succes!")