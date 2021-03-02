from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("HI")

hello = {
    "1":{
        "title": "Kazem",
        "slug": "kazemi",
        "id":12
    }
    ,
    "2":{
        "title": "ff",
        "slug": "f",
        "id":11
    }
}
def api(request):
    return JsonResponse(hello)