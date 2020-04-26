from django.urls import path
from . import views

urlpatterns = [
    path('liveness', views.liveness3, name='liveness'),
    path('readiness', views.readiness3, name='readiness')
]