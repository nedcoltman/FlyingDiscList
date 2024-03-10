from django.shortcuts import render
from django.http import HttpResponse

# Returns some hello world string
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
