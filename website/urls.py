from django.urls import path

from . import views
from . import reception

urlpatterns = [
    path('', views.index, name='index'),
    path('reception/', reception.reception, name='reception'),
    path('greetings/', views.greetings, name='greetings'),
    path('hoopa/', views.hoopa, name='hoopa'),
]
