from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import models
from . import urls

def index(request):
    return render(request, 'index.pug', { 'footer_info': urls.footer_info(request) })

def greetings(request):
    return render(request,'greetings.pug', { 'footer_info': urls.footer_info(request) })

def hoopa(request):
    return render(request,'hoopa.pug', { 'footer_info': urls.footer_info(request) })


# @csrf_exempt
# def list(request):
#     q = request.GET.get('q')
#     items = models.Item.objects.all().order_by('text')
#     if q:
#         items = items.filter(text__icontains=q)
#     return render(request, 'list.pug', {'items': items, 'q': q})


# def item(request, pk):
#     item = models.Item.objects.get(pk=pk)
#     return render(request, 'item.pug', {'item': item})


# def new_item(request):
#     if request.method == 'GET':
#         return render(request, 'new-item.pug')
#     text = request.POST['text']
#     item = models.Item.objects.create(text=text)
#     return redirect('item', pk=item.pk)
