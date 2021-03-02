from django.urls import path
from .views import kazem,api

app_name = "KazemBlog"

urlpatterns = [
    path('', kazem, name="home"),
    path('api/',api,name="api")
]