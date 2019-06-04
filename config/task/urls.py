from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskList.as_view()),
    path('<int:pk>', TaskDetail.as_view()),
    path('<int:pk>/order', OrderCreate.as_view()),
]