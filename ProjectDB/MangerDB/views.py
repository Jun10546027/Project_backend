from django.shortcuts import render,get_object_or_404
from .models import Item

# Create your views here.
def detail(request,post_id):
    detail_title = 'Detail'
    items = get_object_or_404(Item,id=post_id)
    context = {'web_title':detail_title,'items':items}
    return render(request,'detail.html',context)