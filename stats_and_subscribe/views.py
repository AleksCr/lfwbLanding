from django.shortcuts import render
import os
import requests
import logging

from stats_and_subscribe.models import Token

# Create your views here.
from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(format = u'[%(filename)s:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)


def index(request):
    # return HttpResponse("There will be a cool lfwb stats and subscribe landing page")
    logging.debug("page was viewed")
    token = request.GET.get('token')
    if token:
        need_to_save = True
        tokens_list = Token.objects.all()
        items = list(tokens_list.values_list('token', flat=True))
        for s in items:
            if s == token:
                need_to_save = False

        new_token = Token(token=token)
        if need_to_save:
            logging.debug('adding new token: ' + token)
            new_token.save()
        else:
            logging.debug("Current token already exist in database")
    # logging.debug(client_name)
    # logging.debug("This is a debug message")
    # logging.info("Informational message")
    # logging.error("An error has happened!")
    return render(request, 'stats_and_subscribe/index.html')


def service_worker(request):
    path = os.path.join(BASE_DIR, 'files', "firebase-messaging-sw.js")
    js_file = open(path, 'rb')
    response = HttpResponse(js_file, content_type='application/javascript')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'firebase-messaging-sw.js'
    return response


def send(request):
    url = 'http://fcm.googleapis.com/fcm/send'
    t_list = list(Token.objects.all())  # .values_list('token', flat=True))
    for t in t_list:
        logging.debug("tok="+t.token)
        headers = ({
            'Authorization': 'key=AAAAmJY4MBg:APA91bHFlRTUY3RojtBBAVM70abpcWTsKoksgJpog9sdXrmoOP6qUARhOAftXUl4pUV8bAt7iMyiKGnfaTwWcy6_cDz5tO-EChIj62kiDLaS9zbpzmBvemnjUFo9EUSgUzxrpyWQ4HlZ',
            'Content-Type': 'application/json'
        })
        data = ({
            "notification": {
                "title": 'Update',
                "body": 'Click me',
                "icon": 'https://vk.com/images/emoji/D83DDC7B.png',
                "click_action": 'byond://46.188.0.249:1984'
            },
            "to": t.token
        })
        res = requests.post(url, json=data, headers=headers)
        logging.debug(res.text)
    return HttpResponse("There will be a cool lfwb stats and subscribe landing page")