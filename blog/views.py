from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def kazem(request):
    return HttpResponse("HI Gholam")

def api(request):
    data = {
        "title": "مقاله شماره ۱",
        "id": 20,
        "slug": "firstid"
    }
    return JsonResponse(data)
