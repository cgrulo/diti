from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import DetailView, list_detail
from main.models import Page, Section, Product, ProductCategory

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home'),
    url(r'^auto-pull/?$', 'main.views.pull'),
    url(r'^contacto/?$', 'main.views.contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^servicios/?$', list_detail.object_list, {
                                        'queryset' : Page.objects.all(),
                                        'template_name' :'services.html',
                                        }),
    url(r'^servicios/(?P<slug>[^/]+)/$', DetailView.as_view(
                                        model=Page,
                                        template_name="page.html")),
    url(r'^productos/?$', list_detail.object_list, {
                                        'queryset' : ProductCategory.objects.all(),
                                        'template_name' : 'categories.html',
                                        }),
    url(r'^productos/(?P<slug>[^/]+)/$', 'main.views.product_category'), 
    url(r'^(?P<slug>[^/]+)/$', DetailView.as_view(
                                        model=Section,
                                        template_name="section.html")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
