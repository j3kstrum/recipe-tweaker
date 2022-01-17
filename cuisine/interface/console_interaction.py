from cuisine.interface.user_interaction import UserInteraction
from data import RecipeGroup
from interface import Intent
from optimize import Suggestion, Feedback


class ConsoleInteraction(UserInteraction):
    """
    Interacts with the user through the console.
    """

    def gather_intent(self: 'UserInteraction') -> Intent:
        failed = False
        while True:
            if failed:
                print("Sorry, I didn't understand that.")
            request: str = input(
                "What would you like to do? Options are: " + ", ".join(intent.value for intent in Intent)
            )
            for intent in Intent:
                if intent.value == request:
                    return intent
            failed = True

    def create_new_recipe(self: 'UserInteraction') -> RecipeGroup:
        pass

    def select_desired_recipe(self: 'UserInteraction') -> RecipeGroup:
        pass

    def get_feedback(self: 'UserInteraction', on_suggestion: Suggestion) -> Feedback:
        pass
