from cuisine.measurements import Grams


class Ingredient:

    def __init__(self: 'Ingredient', amount: Grams, name: str) -> None:
        self.amount = amount
        self.name = name
