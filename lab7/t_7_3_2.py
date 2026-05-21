class RationalValueError(ValueError):
    def __init__(self, message = "Некоректні дані для арифметичної операції з раціональним числом."):
        self.message = message
        super().__init__(self.message)