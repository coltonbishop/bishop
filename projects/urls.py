from django.urls import path

from . import views

app_name = 'language'
urlpatterns = [
    path('', views.language, name='projects'),
    path('deepmesh', views.language, name='language'),
    path('AlquilandoSuite', views.language, name='language'),
    path('HiveScience', views.language, name='language'),
    path('Rype', views.language, name='language'),
    path('symcnn', views.language, name='language'),
    path('Wengga', views.language, name='language'),
    path('WenggaNet', views.language, name='language'),
    path('Donatello', views.language, name='language'),
    path('Personal', views.language, name='language'),
    path('Esg', views.language, name='language'),
    path('Tigertales', views.language, name='language'),
    path('Puentes', views.language, name='language'),
]



