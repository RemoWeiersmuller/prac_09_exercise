"""Band class stores details to musicians. """

from musician import Musician

class Band:
    def __init__(self, name: str):
        """Construct the class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string of the object."""
        return f"{self.name} {self.musicians}"

    def add(self, musician):
        """Add a new band member."""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            musician.play()