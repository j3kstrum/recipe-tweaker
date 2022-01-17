from cuisine.optimize import Chef
from data import RecipeGroup
from optimize import Suggestion


class BayesianChef(Chef):

    @classmethod
    def of(cls: 'Chef', recipe_group: RecipeGroup) -> 'Chef':
        raise NotImplementedError()

    def suggest(self: 'Chef') -> Suggestion:
        raise NotImplementedError()
