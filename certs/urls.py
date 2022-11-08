from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.cert_check, name='cert_check'),
]
