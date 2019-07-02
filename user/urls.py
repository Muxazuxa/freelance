from django.urls import path
from .views import *

app_name='users'

urlpatterns = [
    path('', UserList.as_view(), name='list'),
    path('<int:pk>', UserDetail.as_view(), name='detail'),
]