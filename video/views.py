from django.shortcuts import render
from .models import Video


# Create your views here.


def video(request):

    video = Video.objects.all

    template = '/video.html'

    return render(request,'template', context ={"video": video})


   
