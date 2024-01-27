from .views import *
from django.urls import path

urlpatterns = [
    path('sign_in/', Registration_new_user.as_view(), name='sign_in'),
    path('log_in/', Authentication_new_user.as_view(), name='log_in'),
    path('get_all_news/', Get_all_news.as_view(), name='get_all_news'),
    path('get_all_category/', Get_all_category.as_view(), name='get_all_category'),
    path('get_image/<int:news_id>/', get_news_image, name='get_news_image'),
    path('save_news/', Save_marked_news.as_view(), name='save_marked_news'),
    path('get_news_cat/', Get_news_cat.as_view(), name='get_news_cat'),
]