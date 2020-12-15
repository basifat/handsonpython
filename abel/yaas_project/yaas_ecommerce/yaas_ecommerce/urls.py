"""yaas_ecommerce URL Configuration

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
from basket import views as Basketviews
from auctions import views as Auctionviews
from yaasusers import views as YaasUsersViews


router = DefaultRouter()
router.register(r'items', Basketviews.ItemViewSet, basename='item')
router.register(r'auctions', Auctionviews.AuctionViewSet, basename='auction')
router.register(r'users', YaasUsersViews.YaasUserViewSet, basename='user')
router.register(r'languages', YaasUsersViews.YaasUserLanguageViewSet, basename='language')
#router.register(r'languages', YaasUsersViews.YaasUserLanguageViewSet, basename='language')



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('tunde', Basketviews.tunde, name='tunde'),
    path('homepage', Basketviews.homepage, name='homepage'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('welcome', YaasUsersViews.welcome, name='welcome'),
    path('language_page/<int:language_id>/', YaasUsersViews.language_page, name='language_page'),
    path('translate_text',YaasUsersViews.translate_text, name='translate_text'),
]




