from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return HttpResponse('домашка к 4 уроку')
