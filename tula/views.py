from django.shortcuts import render
from photologue.models import Gallery


def landing_page(request):
    return render(request, 'landing_page.html', {'decors': Gallery.objects.all()})


# def decor_carousel(request):
#     decors = Decor.objects.all()
#     return render(request, 'decor_carousel.html', {})
