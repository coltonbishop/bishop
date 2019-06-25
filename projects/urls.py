from django.urls import path

from . import views

app_name = 'language'
urlpatterns = [
    path('', views.language, name='projects'),
    path('deepmesh', views.deepmesh, name='language'),
    path('AlquilandoSuite', views.alquilando, name='language'),
    path('HiveScience', views.hive, name='language'),
    path('Rype', views.rype, name='language'),
    path('symcnn', views.symcnn, name='language'),
    path('Wengga', views.wengga, name='language'),
    path('WenggaNet', views.wengganet, name='language'),
    path('Donatello', views.donatello, name='language'),
    path('Personal', views.personal, name='language'),
    path('Esg', views.esg, name='language'),
    path('Tigertales', views.tigertales, name='language'),
    path('Puentes', views.puentes, name='language'),
]



