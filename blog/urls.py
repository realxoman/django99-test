from django.urls import path
from .views import home
app_name = "Kazem"
urlpatterns = [
    path('',home,name="home"),
]
