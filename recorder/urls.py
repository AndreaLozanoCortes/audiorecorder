from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_audio, name='save_audio'),
    path('test/', views.test, name='test'),
    path('download_audio/<int:recording_id>/', views.download_audio, name='download_audio'),
]
