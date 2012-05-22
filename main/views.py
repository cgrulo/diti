from django.shortcuts import render_to_response
from django.http import http_response
from main.models import Slide, Page
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