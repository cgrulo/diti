import os
import commands
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.context_processors import csrf
from main.models import Slide, Page, Product, ProductCategory, ContactForm

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
        if  form.is_valid():
            asunto = request.POST['asunto']
            nombre = request.POST['nombre']
            empresa = request.POST['empresa']
            subject = "[Contacto Diti] %s  (%s de %s)" %(asunto, nombre, empresa)
            email = EmailMessage(subject, request.POST['mensaje'], request.POST['email'], ['contacto@ditisoluciones.com'], ['carlos.roman@ditisoluciones.com', 'fernando.alvarez@ditisoluciones.com', 'arturo.gonzalez@ditisoluciones.com', 'raul.castillo@ditisoluciones.com'], headers={'Reply-To': request.POST['email']})
            email.send()
            return HttpResponseRedirect('/gracias/')
    else:
        form = ContactForm()
    c = {'form' : form }
    c.update(csrf(request))    
    return render_to_response('contact.html', c) 

def product_category(request, slug):
    category = get_object_or_404(ProductCategory, slug=slug)
    return render_to_response('product_category.html', {
        'category': category,
        'products': Product.objects.filter(categoria=category)
    })