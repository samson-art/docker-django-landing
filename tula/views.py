from django.shortcuts import render
from .models import *

nav = NavMenu.objects.all()


def landing_page(request):
    return render(request, 'landing_page.html', {'navs': nav, 'holidays': Holiday.objects.all(), 'trusts': Trust_Us.objects.all(), 'history': History.objects.all()})


# def decor_carousel(request):
#     decors = Decor.objects.all()
#     return render(request, 'decor_carousel.html', {})

def weddings(request):
    return render(request, 'portfolio.html', {'navs': nav, 'portfolio': Holiday.objects.filter(title='Свадьбы').first()})


def price(request):
    return render(request, 'price.html', {'navs': nav})


def graduation(request):
    return render(request, 'portfolio.html', {'navs': nav, 'portfolio': Holiday.objects.filter(title='Выпускные').first()})


def bdays(request):
    return render(request, 'portfolio.html', {'navs': nav, 'portfolio': Holiday.objects.filter(title='Юбилеи').first()})


def kids(request):
    return render(request, 'portfolio.html', {'navs': nav, 'portfolio': Holiday.objects.filter(title='Детское').first()})


def about(request):
    return render(request, 'about.html', {'navs': nav, 'trusts': Trust_Us.objects.all()})