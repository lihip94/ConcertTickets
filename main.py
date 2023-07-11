from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


pdfmetrics.registerFont(TTFont("Alef", "Alef-Regular.ttf"))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT, fontName='Alef', fontSize=10))


def generate_pdf(person, concert_date):
    filename = f"output\\{person}-{concert_date}.pdf"
    # Create a canvas with the specified output file name and page size
    c = canvas.Canvas(filename=filename, pagesize=letter)
    # Set font properties
    c.setFont("Alef", 12)
    c.drawString(50, 700, f"תאריך הקונצרט: {concert_date}"[::-1])
    c.drawString(200, 700, f"שם: {person}"[::-1])
    return c


def add_info_to_pdf(data):

    # Iterate over the data and add it to the PDF
    for concert_date, concert_data in data.items():
        for person, seats in concert_data.items():
            c = generate_pdf(person, concert_date)
            y_position = 670
            for seat in seats:
                row, chair = seat
                c.drawString(70, y_position, f"שורה: {row} | כיסא: {chair}"[::-1])
                y_position -= 20
            y_position -= 20
            # Save the PDF
            c.save()


ticket_data = {
        "17":
            {
                "p1 ": [("1", "8"), ("1", "9")]
            },
        "20":
            {
                "p2": [("2", "1"), ("2", "2")]
            }
    }

add_info_to_pdf(ticket_data)

