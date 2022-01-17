from data.recipe import Recipe
from data import RecipeGroup
from typing import List


class RecipeIO:
    """
    Controls saving and loading of recipes from the filesystem.
    """

    @staticmethod
    def save(recipe: Recipe) -> bool:
        raise NotImplementedError()

    @staticmethod
    def save_completed(recipe: Recipe) -> bool:
        raise NotImplementedError()

    @staticmethod
    def load(recipe_name: str) -> List[Recipe]:
        raise NotImplementedError()

    @staticmethod
    def place_tombstone(recipe_group: RecipeGroup) -> bool:
        raise NotImplementedError()
