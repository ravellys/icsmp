import base64
import io
import urllib

from django.shortcuts import render
from django.views.generic import ListView
from icsmp_project.img3d.models import Img3d
import matplotlib.pyplot as plt

import numpy as np
import requests


class Img3dListView(ListView):
    template_name = "modulos_img3d/modulo_img3d.html"
    model = Img3d
    context_object_name = "img3d"


def open_im_js(im_js):
    resp = requests.get(im_js)
    shape = resp.json()['shape']
    val = resp.json()['im']

    im = np.array(val.split()).astype(int)
    return im.reshape(tuple(shape))


def plot_img(request):
    url = None
    uri = None

    if request.method == 'POST':
        url = request.POST['url']
        # img = open_im_js(url)
        # img = img[0]
        # img = img
        # plt.imshow(img)
        plt.plot(range(21))
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        string = base64.b64encode(buf.read())
        print(buf)
        uri = urllib.parse.quote(string)

    return render(request, 'modulos_img3d/plot_img.html', context={'url': url, 'data': uri})
