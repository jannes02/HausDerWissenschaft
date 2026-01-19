from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet

def draw_flyer(filename):
    width, height = A3  # A3 Hochformat (842x1191 Punkte)

    # Canvas erstellen
    c = canvas.Canvas(filename, pagesize=A3)

    # Platypus Styles
    styles = getSampleStyleSheet()

    date_style = styles['Heading1'].clone("")
    date_style.alignment = TA_RIGHT
    date_style.fontSize = 48
    date_style.textColor = colors.red
    heading_style = styles['Heading1'].clone("")
    heading_style.textColor = colors.red
    heading_style.fontSize = 36

    host_style = styles['Heading2'].clone("")
    host_style.fontSize = 20
    host_style.leading = 22
    title_style = styles['Heading2'].clone("")
    title_style.fontSize = 50
    description_style = styles['Heading2'].clone("")
    description_style.fontSize = 14
    time_style = styles['Heading2'].clone("")
    time_style.alignment = TA_RIGHT
    time_style.fontSize = 20

    # Textbausteine als Paragraphen
    heading = Paragraph("Heute im Haus", heading_style)
    date = Paragraph("04.12.2025", date_style)

    host = Paragraph("Leibnitz-Institut für Werkstofforientierte Technologien<br/>IWT<br/>Bremen", host_style)
    event_time = Paragraph("9:00 Uhr", time_style)
    title = Paragraph("Klausurtagung", title_style)
    description = Paragraph("Im rahmen der Tagung wird über Themen:<br/>  -nachhaltigkeit<br/>  -Produktion<br/>  -Optimierung<br/>gesprochen. Alles wichtige finden Sie auf unserer Website.<br/><br/>Eintritt: 7€", description_style)
    location = Paragraph("Sitzungsraum DG", time_style)

    # frame3_w, frame3_h = veranstaltung_titel_lang.wrap(width-100, 1000)
    # print(f"Benötigte Höhe: {frame3_h}")

    c.setStrokeColor(colors.black)
    c.setLineWidth(5)
    c.line(50, height - 160, width - 50, height - 160)

    c.setStrokeColor(colors.red)
    c.setLineWidth(5)
    c.line(50, height - 590, width - 50, height - 590)

    # Frame um Text an Position zu platzieren (x, y, Breite, Höhe)
    # Achtung: y ist von unten gezählt
    frame_heading = Frame(50, height - 150, width / 2 - 50, 100, showBoundary=0)
    frame_date = Frame(width / 2, height - 150, width / 2 - 50, 100, showBoundary=0)
    frame_host = Frame(50, height - 270, (width-100)*3/4, 100, showBoundary=0)
    frame_time = Frame(width-50-((width-100)*1/4), height - 270, (width - 100) * 1 / 4, 100, showBoundary=0)
    frame_title = Frame(50, height - 380, width - 100, 100, showBoundary=0)
    frame_description = Frame(50, height - 580, (width-100)*3/4, 200, showBoundary=0)
    frame_location = Frame(width-50-((width-100)*1/4), height - 580, (width-100)*1/4, 50, showBoundary=0)
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)


    # Texte in Frames "zeichnen"
    frame_heading.addFromList([heading], c)
    frame_date.addFromList([date], c)
    frame_host.addFromList([host], c)
    frame_time.addFromList([event_time], c)
    frame_title.addFromList([title], c)
    frame_description.addFromList([description], c)
    frame_location.addFromList([location], c)


    # Seite fertigstellen
    c.showPage()
    c.save()

if __name__ == "__main__":
    draw_flyer("flyer_a3.pdf")
