from reportlab.platypus import Frame
from reportlab.lib.pagesizes import A3


class EventDescription:

    def __init__(self, host_name="", title="", description="", time="", location=""):
        self.host_name = host_name
        self.title = title
        self.description = description
        self.time = time
        self.location = location


