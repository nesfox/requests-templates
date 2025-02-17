from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, dish):
    """
    Handles the request to retrieve a recipe for a given dish.

    :param request: The HTTP request object
    :param dish: The name of the dish (string)
    :return: An HttpResponse object with the recipe data or an error message
    """
    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
    except ValueError:
        return HttpResponse("Ошибка! Параметр servings должен быть целым числом.", status=400)

    if servings <= 0:
        return HttpResponse("Ошибка! Количество порций должно быть положительным числом.", status=400)

    recipe_data = DATA.get(dish)

    if not recipe_data:
        return HttpResponse(f'Рецепт для {dish} не найден.', status=404)

    scaled_recipe = {ingredient: quantity * servings for ingredient, quantity in recipe_data.items()}

    context = {
        'recipe': scaled_recipe
    }

    return render(request, 'index.html', context)