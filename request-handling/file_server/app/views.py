import datetime
import re
from django.http import HttpResponse
from django.conf import settings
import os
import datetime
from django.shortcuts import render

files = settings.FILES_DIR
list = os.listdir(files)
def file_list(request, date=None):
    template_name = 'index.html'
    context = {
        'files': [],
        'date': date# Этот параметр необязательный
    }
    if date:
        match = re.search(r"\d{4}-\d\d-\d\d",date)
        filter_date = datetime.datetime.strptime(match[0], '%Y-%m-%d')

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    for name in list:
        stat_info = os.stat(files)
        file_data = {'name': name,
                     'ctime': datetime.datetime.fromtimestamp(stat_info.st_ctime),
                     'mtime': datetime.datetime.fromtimestamp(stat_info.st_mtime)
                     }
        context['files'].append(file_data)
    return render(request, template_name, context)


def file_content(request, name):
    with open(files, 'r') as file:
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file.read()})