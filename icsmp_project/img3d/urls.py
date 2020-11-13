from django.urls import path

from icsmp_project.img3d.views import Img3dListView, plot_img

app_name = 'img3d'
urlpatterns = [
    path('', Img3dListView.as_view(), name='lista_img'),
    path('plot_img/', plot_img, name='plot_img'),
]
