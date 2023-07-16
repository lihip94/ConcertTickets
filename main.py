from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import json
import os


pdfmetrics.registerFont(TTFont("Alef", "Alef-Regular.ttf"))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT, fontName='Alef', fontSize=10))


def generate_pdf(row, seat, name):
    path = f"output\\{name}"
    if not os.path.exists(path):
        os.mkdir(path)
    filename = f"{path}\\{row}-{seat}.pdf"
    # Create a canvas with the specified output file name and page size
    c = canvas.Canvas(filename=filename)
    c.setPageSize((2200, 1700))
    c.drawImage('concertTicket1.jpg', 0, 0)
    # Set font properties
    c.setFont("Alef", 90)
    return c


def add_info_to_pdf():
    data = json.load(open('dataConcert1.json', 'r', encoding='utf-8'))
    # Iterate over the data and add it to the PDF
    for item in data:
        y_position = 270
        if isinstance(item['seats'], str):  # multiple seats
            first_seat, last_seat = item['seats'].split('-')
            seats = list(range(int(first_seat), int(last_seat)+1))
        else:   # only one seat (int parameter)
            seats = [item['seats']]
        row = item['row']
        name = item['name']
        for seat in seats:
            c = generate_pdf(row, seat, name)
            c.drawString(800, y_position, f"{seat}")
            c.drawString(1100, y_position, f"{row}")
            c.drawString(1300, y_position, f"אולם"[::-1])
            c.drawString(900, y_position-200, f"{name}"[::-1])
            # Save the PDF
            c.save()


add_info_to_pdf()

