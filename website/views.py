from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import models
from .forms import ReceptionForm

def index(request):
    return render(request, 'index.pug')
    
def reception(request):
    print(f"'{request.method}'")
    if request.method == 'POST':
        form = ReceptionForm(request.POST)
        if form.is_valid():
            # TODO: process the data in form.cleaned_data as required
            request.session.update(form.cleaned_data)
            # TODO: redirect to a new URL:
            return HttpResponseRedirect('/welcome/')
        else:
            # TODO: Indicate error to user, don't redirect probably
            return HttpResponseRedirect('/error/')
    
    return render(request, 'reception.pug', {'form' : ReceptionForm()})

def greetings(request):
    return render(request,'greetings.pug')

def hoopa(request):
    return render(request,'hoopa.pug')


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
