"""hello_world_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello_world.views import HelloWorldView, LikeView, DislikeView, ResetCounterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HelloWorldView.as_view(), name='index'),
    url(r'^like/$', LikeView.as_view(), name='like'),
    url(r'^dislike/$', DislikeView.as_view(), name='dislike'),
    url(r'^reset/$', ResetCounterView.as_view(), name='reset')
]
