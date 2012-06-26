# -*- coding: utf-8 -*-
from django.db import models
from django import forms

# Create your models here.

class Page(models.Model):
        
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    postimage = models.ImageField(upload_to='img/')
    resumen = models.TextField()
    content = models.TextField()
    index = models.BooleanField()
    
    def __unicode__ (self):
        return self.title
    
class Slide(models.Model):
    
    title = models.CharField(max_length=50)
    imageTitle = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/')
    content = models.TextField()
    url  = models.URLField()
    
    def __unicode__ (self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    
    def __unicode__ (self):
        return self.title
# Blog
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    imagen = models.ImageField(upload_to='img/')
    content = models.TextField()
    
class BlogCategory(models.Model):
    title = models.CharField(max_length=100)
    
# Productos

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    imagen = models.ImageField(upload_to='img/')
    resumen = models.TextField()
    ficha_tecnica = models.FileField(upload_to='files/')
    categoria = models.ForeignKey('main.ProductCategory')
    
    def __unicode__(self):
        return self.title
    
class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='img/')
    
    def __unicode__(self):
        return self.title
   
class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Correo electrónico", required=True)
    empresa = forms.CharField()
    asunto = forms.CharField()
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
    