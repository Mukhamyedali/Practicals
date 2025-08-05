class Band:
    """Band class to store and manage musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            musician.play()
