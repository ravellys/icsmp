from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, v_id):
        self.slug = slug
        self.titulo = titulo
        self.v_id = v_id

    def get_absolute_url(self):
        return reverse("aulas:video", args=(self.slug, ))


videos = [
    Video("video-01", "video 01", "xT9MWktQs2k"),
    Video("video-02", "video 02", "6oEsG5miMsA"),
]

videos_dct = {dct.slug: dct for dct in videos}


def indice(request):
    return render(request, 'aulas/indice.html', context={"videos": videos})


def video(request, slug):
    video_ = videos_dct[slug]
    return render(request, 'aulas/video.html', context={"video": video_})


def palavra_count(request):
    count = None
    palavra = None

    if request.method == 'POST':
        palavra = request.POST['palavra']
        count = len(palavra)

    return render(request, 'aulas/palavra_count.html', context={'count': count, 'palavra': palavra})
