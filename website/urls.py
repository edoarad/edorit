from django.urls import path

from . import views
from . import reception

urlpatterns = []
base_footer_info = []

def add_url(url, handler, name, footer_title):
    urlpatterns.append(path(url, handler, name=name))
    base_footer_info.append({ "url": url, "title": footer_title })

def footer_info(request):
    active_i = 0
    for i in range(len(base_footer_info)):
        if '/'+base_footer_info[i]["url"] == request.path:
            active_i = i
            break
    
    computed = []
    for i in range(len(base_footer_info)):
        cls_str = "is-active" if i == active_i else ("is-complete" if i < active_i else "")
        computed.append({ "title": base_footer_info[i]["title"], "cls_str": cls_str })
    
    return computed

add_url('', views.index, 'index', 'Home'),
add_url('reception/', reception.reception, 'reception', 'Reception'),
add_url('greetings/', views.greetings, 'greetings', 'Greetings'),
add_url('hoopa/', views.hoopa, 'hoopa', 'Hoopa'),
