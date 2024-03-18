from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from fitness_site.models import Video
from fitness_site.serializer import VideoSerializer

def Test(requests):
    if requests.method == 'GET':
        type_ = requests.GET.get('type', None)
        if type_ == 'short':
            return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='short')})
        elif type_ == 'long':
            return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='long')})
        else:
            return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='short')})

    elif requests.method == "POST":
        if requests.POST.get('admin-pass') == '17052008':
            name = requests.POST.get('video_name')
            url = requests.POST.get('video_link')
            type = requests.POST.get('video_length')
            id_video = url.split('/')[-1]
            Video.objects.create(name=name, url=url, type=type, id_video=id_video)
            return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='short')})
        else:
            return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='short')})

class VideosApi(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer