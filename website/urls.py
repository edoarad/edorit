from django.urls import path

from . import views


urlpatterns = [
    path('page1/', views.page1, name='page1'),
    path('list/', views.list, name='list'),
    path('list/new/', views.new_item, name='new-item'),
    path('list/<int:pk>', views.item, name='item'),
    path('', views.index, name='index'),
]
