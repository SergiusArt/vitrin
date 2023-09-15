from django.shortcuts import render


def index(request):
    # context = {
    #     'object_list': Category.objects.all(),
    #     'title': 'Склад товаров',
    #     'view': 'Просмотр товаров',
    # }
    return render(request, 'indicator/index.html')