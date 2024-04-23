from django.urls import path
from .views import index, index2,vida

urlpatterns=[
    path("", index,name="index"),
    path("hola", index2,name="index2"),
    path("vida", vida,name="vida"),
]