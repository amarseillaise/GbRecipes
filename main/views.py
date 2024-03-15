from django.shortcuts import render, redirect, HttpResponse
from .forms import RecipeChoiceForm
from .models import Recipe, Category


# Create your views here.


def index(request):
    tiles = Recipe.objects.all()
    context = {'title': 'Сайт с рецептами', 'main_button_title': 'Новый рецепт', 'tiles': tiles}
    return render(request, 'main/index.html', context)


def details(request, id):
    if request.method == 'GET':
        recipe = Recipe.objects.get(id=id)
        context = {'title': f'{recipe.name}', 'main_button_title': 'На главную', 'recipe': recipe}
        return render(request, 'main/detail.html', context)


def change(request, id):
    if request.method == 'GET':
        recipe = Recipe.objects.get(id=id)
        recipe_forms = RecipeChoiceForm(initial={'name': recipe.name,
                                                 'description': recipe.description,
                                                 'cooking_time': recipe.cooking_time,
                                                 'cooking_descr': recipe.cooking_descr,
                                                 'origin_country': recipe.origin_country,
                                                 'history': recipe.history,
                                                 'image': recipe.image,
                                                 })
        context = {'title': 'Создание рецепта', 'main_button_title': 'На главную', 'form': recipe_forms}
        return render(request, 'main/create.html', context)
    elif request.method == 'POST':
        data = request.POST

        recipe_to_update = Recipe.objects.get(id=id)

        recipe_to_update.name = data['name']
        recipe_to_update.description = data['description']
        recipe_to_update.cooking_time = data['cooking_time']
        recipe_to_update.cooking_descr = data['cooking_descr']
        recipe_to_update.origin_country = Category.objects.get(id=data['origin_country'])
        recipe_to_update.history = data['history']

        try:
            recipe_to_update.image = request.FILES['image']
        except Exception as e:
            print(str(e))

        recipe_to_update.save()

        return redirect('recipies', id=id)


def create(request):
    if request.method == 'GET':
        context = {'title': 'Создание рецепта', 'main_button_title': 'На главную', 'form': RecipeChoiceForm()}
        return render(request, 'main/create.html', context)
    elif request.method == 'POST':
        print(f'uuu - {request.build_absolute_uri()}')
        data = request.POST
        data_to_save = {'name': data['name'],
                        'description': data['description'],
                        'cooking_time': data['cooking_time'],
                        'cooking_descr': data['cooking_descr'],
                        'origin_country': Category.objects.get(id=int(data['origin_country'])),
                        'history': data['history'],
                        }

        try:
            data_to_save['image'] = request.FILES['image']
        except Exception as e:
            print(str(e))
        recipe_to_save = Recipe(**data_to_save)
        recipe_to_save.save()
        return redirect('recipies', id=recipe_to_save.pk)
