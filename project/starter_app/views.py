from django.shortcuts import render
# from .models import Message
import json
from config.settings.base import DJANGO_ROOT


with open(DJANGO_ROOT + '/data/messages.json') as f:
    json_str = f.read()

data = json.loads(json_str)

def home(request):
    # messages = Message.objects.order_by('order')
    context_dict = {
    	'messages': data
    }

    return render(request, 'starter_app/home.html', context_dict)