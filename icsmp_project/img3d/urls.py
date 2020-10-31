from django.urls import path

from icsmp_project.img3d.views import Img3dListView

app_name = 'img3d'
urlpatterns = [
    path('', Img3dListView.as_view(), name='lista_img'),
]
