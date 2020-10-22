from django.urls import path
from . import views


urlpatterns = [
    path('', views.Siren.as_view(), name='index_url'),
    path('post/new/', views.CreateSiren.as_view(), name='create_url'),
    path('post/<int:pk>/edit/', views.UpdateSiren.as_view(), name='update_url'),
    path('post/<int:pk>/', views.DetailSiren.as_view(), name='detail_url'),
    path('post/<int:pk>/delete/', views.DeleteSiren.as_view(), name='delete_url'),

    # api
    path('api/siren/', views.SignallingApi.as_view()),
    # path('api/v1/posts/(?P<pk>[0-9]+)/$', views.PostMember.as_view())
]