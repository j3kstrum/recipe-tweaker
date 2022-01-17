from data import RecipeGroup
from cuisine.optimize import Suggestion
import abc


class Chef(metaclass=abc.ABCMeta):
    """
    Controls the optimization of recipes.
    """

    @classmethod
    @abc.abstractmethod
    def of(cls: 'Chef', recipe_group: RecipeGroup) -> 'Chef':
        raise NotImplementedError()

    @abc.abstractmethod
    def suggest(self: 'Chef') -> Suggestion:
        raise NotImplementedError()
