from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from news_pager.views import *
router = routers.DefaultRouter()

router.register(r'users_admin', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_news/', include('news_pager.urls'))
]
urlpatterns += router.urls