from django.urls import path
from .views import main_view,about_view,media_view,contact_view

urlpatterns = [
    path("",main_view,name="main"),
    path("about/",about_view,name="about"),
    path("contact/",contact_view,name="contact"),
    path("media/",media_view,name="media"),
]
