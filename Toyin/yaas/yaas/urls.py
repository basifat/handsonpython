"""yaas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from yusers import views



router = DefaultRouter()
#router.register(r'info', views.ActorsViewSet, basename='info')


urlpatterns = [path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('create/', views.ActorCreateAPIView.as_view(), name='create'),
    path('get/<int:actor_id>', views.ActorGetAPIView.as_view(), name='get'),
    path('update/<int:actor_id>', views.ActorUpdateAPIView.as_view(), name='update'),
    path('delete/<int:actor_id>', views.ActorDeleteAPIView.as_view(), name='delete'),
    #path('createuser/', views.DancingCreateView.as_view(), name='yuserscreate'),
    #path('users', views.ActorsDetail.as_view(), name='users'),
    path('user/', views.ActorsView.as_view(), name='user'),
    path('users/<int:actor_id>', views.ActorsDetail.as_view(), name='users'),
    #path('debs', views.debby, name='debs'),
    
]
