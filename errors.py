class NoInfoError(Exception):
    def __init__(self):
        super().__init__("NoInfoError : There is no DATA.")

class WeekendError(Exception):
    def __init__(self):
        super().__init__("WeekendError : It is weekend")

