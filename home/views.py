from django.http import HttpResponse
from django.shortcuts import render


def homeview(request):
    return render(request,'home/index.html')