from cuisine.optimize import Feedback
from data.recipe import Recipe


class Suggestion:

    def with_feedback(self: 'Suggestion', feedback: Feedback) -> Recipe:
        pass
