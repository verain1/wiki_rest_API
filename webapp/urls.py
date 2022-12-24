from django.urls import path, include
from .views import *

urlpatterns = [
    path('/', homePageView),
    path('/<str:id>', ansPageView)
]
