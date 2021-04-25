from django.shortcuts import render
from .models import Video

# Create your views here.
def video(request):
    video=Video.objects.all()
    return render(request,"video.html",{"video":video})