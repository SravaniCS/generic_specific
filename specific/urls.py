from django.urls import path
from specific.views import *

app_name='specific'

urlpatterns=[
    path('specificpage1/',specificpage1,name='specificpage1'),
    path('specificpage2/',specificpage2,name='specificpage2'),
]