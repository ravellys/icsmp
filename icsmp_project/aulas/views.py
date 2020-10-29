from django.shortcuts import render, get_object_or_404

from icsmp_project.aulas.models import Video


def indice(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'aulas/indice.html', context={"videos": videos})


def video(request, slug):
    video_ = get_object_or_404(Video, slug=slug)
    return render(request, 'aulas/video.html', context={"video": video_})


def palavra_count(request):
    count = None
    palavra = None

    if request.method == 'POST':
        palavra = request.POST['palavra']
        count = len(palavra)

    return render(request, 'aulas/palavra_count.html', context={'count': count, 'palavra': palavra})
