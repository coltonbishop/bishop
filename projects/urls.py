from django.urls import path

from . import views

app_name = 'language'
urlpatterns = [
    path('', views.language, name='projects'),
    path('deepmesh', views.deepmesh, name='language'),
    path('alquilando', views.alquilando, name='language'),
    path('hivescience', views.hive, name='language'),
    path('rype', views.rype, name='language'),
    path('symcnn', views.symcnn, name='language'),
    path('wengga', views.wengga, name='language'),
    path('wengganet', views.wengganet, name='language'),
    path('donatello', views.donatello, name='language'),
    path('personal', views.personal, name='language'),
    path('esg', views.esg, name='language'),
    path('tigertales', views.tigertales, name='language'),
    path('puentes', views.puentes, name='language'),
    path('pokedex', views.pokedex, name='language'),
    path('activelearning', views.activelearning, name='language'),
    path('nmt', views.nmt, name='language'),
]



