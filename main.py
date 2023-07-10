from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def generate_pdf(person, concert_date):
    filename = f"{person}-{concert_date}.pdf"
    # Create a canvas with the specified output file name and page size
    c = canvas.Canvas(filename=filename, pagesize=letter)
    # Set font properties
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Concert Date: {concert_date}")
    c.drawString(200, 700, f"Person name: {person}")
    return c


def add_info_to_pdf(data):

    # Iterate over the data and add it to the PDF
    for concert_date, concert_data in data.items():
        for person, seats in concert_data.items():
            c = generate_pdf(person, concert_date)
            y_position = 670
            for seat in seats:
                row, chair = seat
                c.drawString(70, y_position, f"Row: {row} | Chair: {chair}")
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

