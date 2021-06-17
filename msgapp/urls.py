# 作者：宁方笑
# 开发时间：2021/6/14 21:36
from django.urls import path
from . import views

urlpatterns = [
    path('', views.msgproc),
]