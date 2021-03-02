from django.urls import path
from .views import home,api

app_name = "Kazem"
urlpatterns = [
    path('',home,name="home"),
    path('api/',api,name="api")
]
