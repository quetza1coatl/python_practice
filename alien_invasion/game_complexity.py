import enum


class GameComplexity(enum.Enum):
    easy = (0, 'Easy')
    normal = (1, 'Normal')
    hard = (2, 'Hard')

    def __init__(self, complexity_factor, title):
        self.complexity_factor = complexity_factor
        self.title = title
