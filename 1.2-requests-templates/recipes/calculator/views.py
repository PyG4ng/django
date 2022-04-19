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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_view(request, param):
    amount = int(request.GET.get("servings", 1)) if request.GET.get("servings").isdigit() else 1
    data = DATA.get(f"{param}")

    recipe = {}
    if data is not None:
        recipe = {item: round(quantity * amount, 2) for item, quantity in data.items()}

    # if data is None:
    #     return HttpResponse(f'No recipe for {param}')

    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
