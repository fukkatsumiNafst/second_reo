from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adv
from .forms import AdvForms
from django.urls import reverse

def index(requset):
    adv = Adv.object.all()
    context = {'adv': adv}
    return render(request, 'index.html', context)


def top_sellers(requset):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvForms(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:    
        form = AdvForms()
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)