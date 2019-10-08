from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime as dt
from os import listdir as ls


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse(home_view),
        'Показать текущее время': reverse(time_view),
        'Показать содержимое рабочей директории': reverse(workdir_view)
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = dt.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    current_list = ls(path=".")
    msg = f'Список файлов в рабочей директории: {current_list}'
    return HttpResponse(msg)
