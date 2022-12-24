import json
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.



# def homePageView(request):
#     return HttpResponse(json.dumps(dict_temp))

def ansPageView(request, id):
    return HttpResponse(id)