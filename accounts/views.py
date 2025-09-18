from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def users_list(request):
    return HttpResponse("Hello accounts apis") 