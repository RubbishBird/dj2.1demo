'''为应用程序users定义url模式'''

from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views

#修改模板路径
LoginView.template_name = 'users/login.html'

app_name='[users]'
urlpatterns = [
    #登录页面
    path('login/',LoginView.as_view(),name='login'),
]