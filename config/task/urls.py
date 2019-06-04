from django.urls import path
from .views import *

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('<int:pk>', TaskDetail.as_view(), name='detail'),
    path('<int:pk>/order', OrderCreate.as_view(), name='order'),
]