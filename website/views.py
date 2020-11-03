import io
import json

from django.core.files import File
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)

from . import models
from . import urls


def index(request):
    return render(request, 'index.pug', { 'footer_info': urls.footer_info(request) })


def greetings(request):
    return render(request,'greetings.pug', { 'footer_info': urls.footer_info(request) })
def invitation(request):
    return render(request,'invitation.pug', { 'footer_info': urls.footer_info(request) })

def bar(request):
    return render(request,'bar.pug', { 'footer_info': urls.footer_info(request) })


def hoopa(request):
    return render(request,'hoopa.pug', { 'footer_info': urls.footer_info(request) })


def react_example(request):
    return render(request, 'react-example.pug', dict(
        footer_info = {'dots': []}, # Suppress footer.
    ))


def dancefloor(request):
    return render(request, 'dancefloor.pug', dict(
        dancers = models.Dancer.objects.all(),
        footer_info = urls.footer_info(request),
    ))


@csrf_exempt
def add_dancer(request):
    dancer = models.Dancer.objects.create()
    with io.BytesIO(request.body) as fp:
        dancer.video.save(f'{dancer.id}.webm', File(fp), True)
    dancer.save()
    return JsonResponse({'id': dancer.id})


@csrf_exempt
def position_dancer(request):
    data = json.loads(request.body)
    dancer = models.Dancer.objects.get(id=data['id'])
    dancer.offset_top = data['offset_top']
    dancer.offset_left = data['offset_left']
    dancer.save()
    return HttpResponse('')