from reportlab.platypus import Frame
from reportlab.lib.pagesizes import A3


class EventDescription(Frame):
    host_name = ""
    title = ""
    description = ""
    time = ""
    is_public = True
    location = ""
    is_red = False

    def __init__(self, x1: float, y1: float):
        width, height = A3
        super().__init__(x1, y1, width, height)

    def build_frame(self):
        pass

