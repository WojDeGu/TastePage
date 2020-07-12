from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi! In the future you create the recipes.")