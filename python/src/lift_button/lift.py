class Lift:
    def __init__(self):
        self.lights = "OFF"
        self.doors = "CLOSED"

    def press_button(self):
        self.lights = "ON"

    def arrive(self):
        self.doors = "OPEN"
