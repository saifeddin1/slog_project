from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='slog-home'),
    path('about/', views.about, name='slog-about'),

]
