from django.urls import path

from training import views
from training.views import index

app_name = 'training'

urlpatterns = [
    path("<str:name_training>", index),
    ]