from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from . import models


def index(request):
    return render(request, 'index.pug')


def page1(request):
    return render(request, 'page1.pug')


@csrf_exempt
def list(request):
    q = request.GET.get('q')
    items = models.Item.objects.all().order_by('text')
    if q:
        items = items.filter(text__icontains=q)
    return render(request, 'list.pug', {'items': items, 'q': q})


def item(request, pk):
    item = models.Item.objects.get(pk=pk)
    return render(request, 'item.pug', {'item': item})


def new_item(request):
    if request.method == 'GET':
        return render(request, 'new-item.pug')
    text = request.POST['text']
    item = models.Item.objects.create(text=text)
    return redirect('item', pk=item.pk)
