from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("There will be a cool lfwb stats and subscribe landing page")
    return render(request, 'stats_and_subscribe/index.html')
