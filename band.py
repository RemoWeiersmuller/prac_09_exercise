"""Band class stores details to musicians. """


class Band:
    def __init__(self, name: str):
        """Construct the class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string of the object."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a new band member."""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            player = musician.play()
            print(player)
