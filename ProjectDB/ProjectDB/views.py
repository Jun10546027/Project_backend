from django.shortcuts import render
from MangerDB.serializers import data
import json
from MangerDB.models import Item

def homepage(request):
    homepage_title = 'My homepage'
    items = Item.objects.all()
    json_list = json.loads(data)
    return render(request,'index.html',{'web_title':homepage_title,'items_lists':json_list,'items':items})