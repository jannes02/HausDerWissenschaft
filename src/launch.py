from src.backend.event_description import EventDescription
from src.backend.flyer_builder import FlyerBuilder


if __name__ == "__main__":
    #draw_flyer("flyer_a3.pdf")
    event1 = EventDescription(
        "Leibnitz-Institut für Werkstofforientierte Technologien<br/>IWT<br/>Bremen>",
        "Klausurtagung",
    "Im rahmen der Tagung wird<br/><br/><br/><br/><br/><br/><br/><br/> über Themen:<br/>  -nachhaltigkeit<br/>  -Produktion<br/>  -Optimierung<br/>gesprochen. Alles wichtige finden Sie auf unserer Website.<br/><br/>Eintritt: 7€",
        "12:30",
        "Sitzungsraum DG")

    event2 = EventDescription(
        "Leibnitz-Institut für Werkstofforientierte Technologien 2",
        "Besprechung",
        "-Optimierung<br/>gesprochen. Alles wichtige finden Sie auf unserer Website.<br/><br/>Eintritt: 7€",
        "15:30",
        "Sitzungsraum 3")

    builder = FlyerBuilder("HDW-Flyer1.pdf")
    builder.is_debug = True
    builder.build(event_descriptions=[event1])
