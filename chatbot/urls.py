from django.urls import path
from .views import *

app_name='chatbot'

urlpatterns = [
    path('start/',start,name="start"),
    path('service/', service ,name="service"),
    path('category/',category,name="category"),
    path('question/',question,name="question"),
]