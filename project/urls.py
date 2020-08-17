from django.urls import include, path


urlpatterns = [
    path('', include('website.urls')),
]
