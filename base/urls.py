from django.urls import path
from . import views

urlpatterns = [
    path('',views.looby),
    path('room/',views.room),
]
