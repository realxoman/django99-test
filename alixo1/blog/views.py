from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context={
        "articles":[
            {
                "title":"HI",
                "id":12,
                "content": "Hello World"
            },{
                "title":"Hello",
                "id":13,
                "content": "Hello Guys"
            },{
                "title":"Hello",
                "id":13,
                "content": "Hello Guys"
            }
        ]
    }
    return render(request,"blog/home.html",context)