from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import models
from .forms import ReceptionForm

def reception(request):
    if request.method == 'POST':
        form = ReceptionForm(request.POST)
        if form.is_valid():
            # TODO: process the data in form.cleaned_data as required
            print(f"New guest registered with details: {form.cleaned_data}")
            request.session.update(form.cleaned_data)
            register_guest_db(form.cleaned_data)
            # TODO: redirect to a new URL:
            return HttpResponseRedirect('/welcome/')
        else:
            # TODO: Indicate error to user, don't redirect probably
            return render(request, 'reception.pug', {'form' : form})
    
    return render(request, 'reception.pug', {'form' : ReceptionForm()})


def register_guest_db(form_data):
    if models.Guest.objects.filter(name=form_data['name']):
        print("Name collision found!")
        # TODO: Make this show an error to the user
        raise Exception("Name already taken!")

    new_guest = models.Guest(
        name=form_data['name'],
        table_name=form_data['table_name'],
        photo_path="", # TODO: Upload photo and fill this in on submit
    )
    
    new_guest.save()