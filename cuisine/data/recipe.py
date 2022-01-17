from ingredient import Ingredient
from typing import List
from cuisine.optimize import Feedback


class Recipe:

    def __init__(self: 'Recipe', name: str, ingredients: List[Ingredient], feedback: Feedback = None):
        self.name = name
        self.ingredients = ingredients
        self.feedback = feedback
