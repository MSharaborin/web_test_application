from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('siren/', views.SirenListView.as_view(), name='siren_list'),
    path('siren/<pk>/', views.SirenDetailView.as_view(), name='siren_detail'),
]