from django.shortcuts import render
import os
import requests

# Create your views here.
from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    # return HttpResponse("There will be a cool lfwb stats and subscribe landing page")
    print("page was viewed")
    client_name = request.GET.get('token')
    print(client_name)
    return render(request, 'stats_and_subscribe/index.html')


def service_worker(request):
    path = os.path.join(BASE_DIR, 'files', "firebase-messaging-sw.js")
    js_file = open(path, 'rb')
    response = HttpResponse(js_file, content_type='application/javascript')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'firebase-messaging-sw.js'
    return response