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

from basket import views as BasketViews
from auctions import views as AuctionViews
from yaasusers import views as YaasUserViews 
from django.conf.urls.i18n import i18n_patterns 

router = DefaultRouter()
router.register(r'items', BasketViews.ItemViewSet, basename='item')
router.register(r'auctions', AuctionViews.AuctionViewSet, basename='auction')
router.register(r'users', YaasUserViews.YaasUserViewSet, basename='user')
router.register(r'languages', YaasUserViews.YaasUserLanguageViewSet, basename='language')



# i18n_patterns(
urlpatterns = [path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('tunde', BasketViews.tundefn, name='tundefn-udid'),
    path('homepage', BasketViews.homepage, name='homepage'),
    path('welcome', YaasUserViews.welcome, name='welcome'),
    path('language_page/<int:language_id>/', YaasUserViews.language_page, name='language_page'),
    path('translate_text',YaasUserViews.translate_text, name='translate_text'),
    # path('api-auth', include('rest_framework.urls'))
]




