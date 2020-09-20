from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reception/', views.reception, name='reception'),
    path('greetings/', views.greetings, name='greetings'),
    path('hoopa/', views.hoopa, name='hoopa'),

    # Ideas:
    # Footer - Terms & conditions.
    #     Something silly like a marriage agreement.
    # Popup - Do you approve the use of cookies?
    #     yes button - orit with cookies. No button, Edo with lattice.
    # Bar - Lots of Corona bottles. Can drink shots - each shot, the screen starts to be more fuzzy and move around for the entire wedding.
    # Talk with people - Rabbi, grandmas, parents, ...
    # Coronavirus attack!! - suddenly, the world turns green. An alert message tells you that there is a virus attack, and you need to fire UV on little covid viruses to kill them all.
    # Side adventures - in the periphery, mom drinks and becomes drunk more and more over time.
    # Patting zone - place where kittens purr
    # Desserts - gallery of Orit's dessert photos.
    # Dance floor - people can take videos of themselves and then the dance floor will be filled with GIFs of people dancing. (Perhaps some moderation would be helpful)
    # Magnet board - contains a bunch of photos of people with blank faces. people can add their faces in via webcam and save the photo.


    # # Examples
    # path('list/', views.list, name='list'),
    # path('list/new/', views.new_item, name='new-item'),
    # path('list/<int:pk>', views.item, name='item'),
]
