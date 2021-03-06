from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from . import reception
from . import magnets
from . import table
from . import greetings


urlpatterns = []
base_footer_info = []


def add_url(url, handler, name, footer_title=None):
    urlpatterns.append(path(url, handler, name=name))
    if footer_title:
        base_footer_info.append({ "url": "/" + url, "title": footer_title })


def footer_info(request):
    active_i = 0
    for i in range(len(base_footer_info)):
        if base_footer_info[i]["url"] == request.path:
            active_i = i
            break
    
    next_page = None
    if i+1 < len(base_footer_info):
        next_page = base_footer_info[i+1]["url"]

    dots = []
    for i in range(len(base_footer_info)):
        info = base_footer_info[i].copy()
        info["cls_str"] = "is-active" if i == active_i else ("is-complete" if i < active_i else "")
        dots.append(info)
    
    return { "dots": dots, "next_page": next_page }


add_url('', views.index, 'index', 'Home')
add_url('invitation/', views.invitation, 'invitation', 'Invitation')
add_url('reception/', reception.reception, 'reception', 'Reception')
add_url('table/', table.table, 'table', 'Table')
add_url('greetings/', greetings.greetings, 'greetings', 'Greetings')
add_url('hoopa/', views.hoopa, 'hoopa', 'Hoopa')
add_url('dancefloor/', views.dancefloor, 'dancefloor', 'Dancefloor')


add_url('react-example/', views.react_example, 'react-example')
add_url('api/dancefloor/add-dancer', views.add_dancer, 'add-dancer')
add_url('api/dancefloor/position-dancer', views.position_dancer, 'position-dancer')


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
add_url('magnets/', magnets.magnets, 'magnets', 'Magnets')
add_url('bar/', views.bar, 'bar', 'Bar')
