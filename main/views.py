from django.shortcuts import render

def main_view(request):
    return render(request,"views/index.html")

def about_view(request):
    return render(request,"views/about.html")

def contact_view(request):
    return render(request,"views/contact.html")

def media_view(request):
    return render(request,"views/media.html")