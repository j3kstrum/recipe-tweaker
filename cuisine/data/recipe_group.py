from typing import List

from data import Recipe
from data.ingredient_group import IngredientGroup
from interface.recipe_io import RecipeIO


class RecipeGroup:

    def __init__(self: 'RecipeGroup', name: str, ingredients: List[IngredientGroup]) -> None:
        self.name = name
        self.ingredients = ingredients
        self.trials: List[Recipe] = self.history()

    def history(self: 'RecipeGroup') -> List[Recipe]:
        return RecipeIO.load(self.name)

    def save(self: 'RecipeGroup') -> bool:
        all_successful = True
        for trial in self.trials:
            all_successful = all_successful and RecipeIO.save(trial)
        return all_successful