from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hadeel',views.hadeel)
]