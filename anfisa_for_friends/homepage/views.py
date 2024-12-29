from django.shortcuts import render # type: ignore
#from django.db.models import Q # type: ignore

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.values(
        'id','title','description'
        ).filter(
        is_on_main=True, is_published=True
        ).order_by('title')[1:4]
    
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context) 
