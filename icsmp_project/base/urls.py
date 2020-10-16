from django.urls import path

from icsmp_project.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
