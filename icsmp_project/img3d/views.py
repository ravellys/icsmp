from django.views.generic import ListView
from icsmp_project.img3d.models import Img3d


class Img3dListView(ListView):
    template_name = "modulos_img3d/modulo_img3d.html"
    model = Img3d
    context_object_name = "img3d"
