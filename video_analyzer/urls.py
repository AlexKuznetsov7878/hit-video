from django.urls import path
from . import views
app_name = "video_analyzer"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('video_create/', views.video_create, name='video_create')
]