from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("story", views.story, name="story"),
    path("products", views.products, name="products"),
    path("salas", views.salas, name="salas"),
    path("gabinetes", views.gabinetes, name="gabinetes"),
    path("cias", views.cias, name="cias"),
    path("escritorios", views.escritorios, name="escritorios"),
    path("comedor", views.comedor, name="comedor"),
    path("ninos", views.ninos, name="ninos"),

    #API Routes
    path("emails", views.emails, name="emails")
]
