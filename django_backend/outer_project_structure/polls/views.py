from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def second_view(request):
    return HttpResponse("this is very good shit here")