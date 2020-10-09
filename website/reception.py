import base64

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import models
from . import urls
from .forms import ReceptionForm

def reception(request):
    if request.method == 'POST':
        form = ReceptionForm(request.POST, request.FILES)
        print(f"Form submitted: {form.data}")
        if form.is_valid():
            # TODO: process the data in form.cleaned_data as required
            print(f"New guest registered with details: {form.cleaned_data}")
            request.session.update(form.cleaned_data)
            guest_id = register_guest_db(form.cleaned_data)
            request.session['guest_id'] = guest_id

            # TODO: redirect to a new URL:
            return HttpResponseRedirect('/welcome/')
        else:
            print(f"Got invalid form: {form.errors}")
    else:
        form = ReceptionForm()
    return render(request, 'reception.pug', { 'form' : form, 'footer_info': urls.footer_info(request)})


def guest_name_to_filename(guest_name : str) -> str:
    # TODO: This is not really clean and might not work as a file name
    return guest_name.replace(" ", "_")

def register_guest_db(form_data):
    if models.Guest.objects.filter(name=form_data['name']):
        print("Name collision found!")
        # TODO: Make this show an error to the user
        raise Exception("Name already taken!")

    image_format, image_b64 = form_data['photo'].split(';base64,') 
    ext = image_format.split('/')[-1]
    # TODO: Raise error to user if he tried to submit not a png because he is trying to hack us :)
    # TODO: In general this image upload should be well-protected as it is a classic vulnerability
    photo_filename = guest_name_to_filename(form_data['name']) + ".png"
    photo_file = ContentFile(base64.b64decode(image_b64), name=photo_filename)
    new_guest = models.Guest(
        name=form_data['name'],
        table_name=form_data['table_name'],
        photo = photo_file, # TODO: Upload photo and fill this in on submit
    )
    
    new_guest.save()
    return new_guest.id