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


def send(request):
    client_name = request.GET.get('token')
    print(client_name)
    url = 'http://fcm.googleapis.com/fcm/send'
    headers = ({
        'Authorization': 'key=AAAAmJY4MBg:APA91bHFlRTUY3RojtBBAVM70abpcWTsKoksgJpog9sdXrmoOP6qUARhOAftXUl4pUV8bAt7iMyiKGnfaTwWcy6_cDz5tO-EChIj62kiDLaS9zbpzmBvemnjUFo9EUSgUzxrpyWQ4HlZ',
        'Content-Type': 'application/json'
    })
    data = ({
        "notification": {
            "title": 'Ruzone',
            "body": 'Великая Миграция!',
            "icon": 'http://lfwb.ru/images/9/99/Migrant.png',
            "click_action": ''
        },
        "to": 'eyz5xabsduE:APA91bEO_HWWbr5FQdFRVmxoPeoTb980clGzXuvlrWD0s1_vz0O2zVzT5CF6kTC5TgP-v6BZoF7_GTFnT58aMGM8jCd5PceK0BWFzxEM3kTtnmMjMRuzYEtZcC0IU6ks6OjedawD5U2k'
    })
    res = requests.post(url, json=data, headers=headers)
    print(res.text)
    return HttpResponse("There will be a cool lfwb stats and subscribe landing page")