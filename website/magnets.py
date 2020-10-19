import base64

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import models
from . import urls
from .forms import ReceptionForm

def magnets(request):
    return render(request, 'magnets.pug', { 'footer_info': urls.footer_info(request) })