from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "Hello, Welcome to world of Data Science and Machine Learning")
