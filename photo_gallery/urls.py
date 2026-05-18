from django.urls import path
from django.http import HttpResponse


def placeholder(request):
    return HttpResponse("Gallery coming soon!")


urlpatterns = [
    path('', placeholder, name='gallery'),
]