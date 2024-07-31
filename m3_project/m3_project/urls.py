from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render

from m3 import get_app_urlpatterns

def workspace(request):
	"""
	Возвращает view для отображения Рабочего Стола на
	основе шаблона m3
	"""
	return render(
    	    request,
    	    'm3_workspace.html',
    	    context={'debug': settings.DEBUG},
	)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', workspace),
]

# Собираем шаблоны урлов из app_meta
# подключенных приложений
urlpatterns.extend(get_app_urlpatterns())