from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import models
from . import urls
from .forms import GreetingsForm

def greetings(request):
    # TODO: ensure that the user is signed in so that we have a guest_id
    if request.method == 'POST':
        form = GreetingsForm(request.POST)
        if form.is_valid():
            save_new_greeting(form.cleaned_data, request.session['guest_id'])
        else:
            print(f"Got invalid form: {form.errors}")
    else:
        form = GreetingsForm()
    return render(request,'greetings.pug', { 'form': form, 'footer_info': urls.footer_info(request) })

def save_new_greeting(form_data, guest_id):
    new_greeting = models.Greeting(
        message=form_data['message'],
        private=form_data['private'],
    )
    new_greeting.guest_id = guest_id
    
    new_greeting.save()
    return new_greeting.id