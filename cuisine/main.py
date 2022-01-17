from cuisine.interface import UserInteraction, ConsoleInteraction, Intent, RecipeIO
from cuisine.data import RecipeGroup, Recipe
from cuisine.optimize import Chef, Suggestion, BayesianChef, Feedback


if __name__ == '__main__':
    # We want to be able to work on perfecting any recipe at any point in time.
    while True:
        user_interaction: UserInteraction = ConsoleInteraction()
        intent: Intent = user_interaction.gather_intent()
        if intent == Intent.CREATE_NEW_RECIPE:
            new_recipe: RecipeGroup = user_interaction.create_new_recipe()
            intent = Intent.IMPROVE_EXISTING
        if intent == Intent.IMPROVE_EXISTING:
            recipe_group: RecipeGroup = user_interaction.select_desired_recipe()
            chef: Chef = BayesianChef.of(recipe_group)
            suggestion: Suggestion = chef.suggest()
            feedback: Feedback = user_interaction.get_feedback(suggestion)
            result: Recipe = suggestion.with_feedback(feedback)
            RecipeIO.save(result)
        if intent == Intent.RECYCLE_RECIPE:
            recipe_group: RecipeGroup = user_interaction.select_desired_recipe()
            RecipeIO.place_tombstone(recipe_group)
