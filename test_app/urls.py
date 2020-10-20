from django.urls import path
from . import views


urlpatterns = [
    path('', views.Siren.as_view())
]