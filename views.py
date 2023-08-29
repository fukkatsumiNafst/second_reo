from django.shortcuts import render
from django.http import HttpResponse
from .models import Adv

def index(requset):
    adv = Adv.object.all()
    context = {'adv': adv}
    return render(request, 'index.html', context)


def top_sellers(requset):
    return render(request, 'top-sellers.html')