from django.shortcuts import render


# Create your views here.


def glavn_stran(request):
    title = 'Главная страница'
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'title_h1': title, 'title_lice': lice_1,
               'shop': lice_2, 'corzina': lice_3}
    return render(request, 'Glavn_stran.html', context)


def shop_stran(request):
    title_shop = 'Это магазин'
    game_1 = 'Portal 3'
    game_2 = 'Half life 3'
    game_3 = 'Warcraft 4'
    context = {'title_h1': title_shop,
               'game_1': game_1,
               'game_2': game_2,
               'game_3': game_3}
    return render(request, 'Shop_stran.html', context)


def corzina_stran(request):
    title_corzina = 'Это корзина'
    context = {'title_h1': title_corzina}
    return render(request, 'Corzina.html', context)