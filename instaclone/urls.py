"""instaclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from instaclone import settings
from instaclone import views
from account import views as aviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexFeedView,name='index'),
    # path('feed',views.FeedView,name='feed'),
    # path('feed/<pk>',views.FeedView,name='feed'),
    path('account/',include('account.urls')),
    path('like-post/',aviews.postLikeView,name='like-post'),
    path('follow/',aviews.follow,name='follow'),
    path('unfollow/',aviews.unfollow,name='unfollow'),
    path('accdel/',aviews.AccDelView,name='account_delete_msg'),
    path('search',aviews.SearchView,name='search'),
    


]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
