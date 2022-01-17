import abc
from cuisine.interface.intent import Intent
from cuisine.data import RecipeGroup
from cuisine.optimize import Suggestion, Feedback


class UserInteraction(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def gather_intent(self: 'UserInteraction') -> Intent:
        raise NotImplementedError()

    @abc.abstractmethod
    def create_new_recipe(self: 'UserInteraction') -> RecipeGroup:
        raise NotImplementedError()

    @abc.abstractmethod
    def select_desired_recipe(self: 'UserInteraction') -> RecipeGroup:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_feedback(self: 'UserInteraction', on_suggestion: Suggestion) -> Feedback:
        raise NotImplementedError()
