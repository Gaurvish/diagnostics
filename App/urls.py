from django.urls import path
from .views import *

urlpatterns = [
    path('',Index,name='index'),
    path('about/',About,name='about'),
    path('doctor/',Doctor,name='doctor'),
    path('services/',Services,name='services'),
    path('contact/',Contact,name='contact'),
    path('blog/',Blog,name='blog')
]
