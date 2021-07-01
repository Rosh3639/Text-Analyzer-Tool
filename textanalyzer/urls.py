
from django.urls import path
from textanalyzer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('analyze', views.analyze, name='analyze'),
    path('contact', views.contact, name='contact'),
]