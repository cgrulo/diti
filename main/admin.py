from django.contrib import admin
from main.models import Page, Slide, Section, Product, ProductCategory

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/textareas.js')

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}   
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/textareas.js')

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/textareas.js') 

admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Slide)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)