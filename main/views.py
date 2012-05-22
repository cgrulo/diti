from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Slide, Page, ContactForm
import os
import commands


def home(request):
    response = {
        "slides_list": Slide.objects.all(),
        "pages_list": Page.objects.all(),
    }
    return render_to_response('index.html', response)

def pull(request):
	os.chdir(os.path.dirname(os.path.dirname(__file__)))
	gitpull = commands.getstatusoutput('git pull')[1]

	return HttpResponse(gitpull)
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        return HttResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        
    return render_to_response('contact.html', { 'form' : form,}) 