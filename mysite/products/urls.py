from django.urls import path
from  .views import *

urlpatterns = [
    path('<int:pageid>/', page),
    path('product/<str:userRequest>/', products)
]