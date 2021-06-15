"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.edit import CreateView
from blog.views import NewsList, NewsDetail, Search, NewsCreate, NewsEdit, NewsDelete
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', NewsList.as_view()),
    path('news/<pk>', NewsDetail.as_view(),name='new_detail'),
    path('search', Search.as_view(),name='search'),
    path('news/create/', NewsCreate.as_view(),name='new_create'),
    path('news/update/<pk>', NewsEdit.as_view(),name='new_edit'),
    path('news/<pk>/delete', NewsDelete.as_view(),name='delete_news'),
]
