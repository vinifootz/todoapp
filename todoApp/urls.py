"""todoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import signupuser, currenttodos, logoutuser,loginuser, home, createtodo, viewtodo, completetodo, deletetodo, completedtodos



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    #paginação
    path('signup/', signupuser, name='signupuser'),
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('current/', currenttodos, name='currenttodos'),
    path('completed/', completedtodos, name='completedtodos'),
    #CRUd
    path('create/', createtodo, name='createtodo'),
    path('todo/<int:todo_pk>', viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', deletetodo, name='deletetodo'),

]
