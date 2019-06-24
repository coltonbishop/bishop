from django.urls import path

from . import views

app_name = 'language'
urlpatterns = [
    path('', views.language, name='language'),
]