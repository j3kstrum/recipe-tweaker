from measurements import Grams


class IngredientGroup:

    def __init__(self: 'IngredientGroup', low: Grams, high: Grams, name: str) -> None:
        if low > high:
            raise ValueError("Lowest value for an ingredient cannot be higher than the highest value.")
        self.low = low
        self.high = high
        self.name = name

    def normalize(self: 'IngredientGroup', value: Grams) -> float:
        if not self.low <= value <= self.high:
            raise ValueError("Cannot normalize a value outside of the ingredient bounds.")
        return (value - self.low) / (self.high - self.low)

    def unnormalize(self: 'IngredientGroup', value: float) -> Grams:
        if not 0 <= value <= 1:
            raise ValueError("Normalized value was outside of acceptable range 0 to 1.")

        return self.low + (self.high - self.low) * value
