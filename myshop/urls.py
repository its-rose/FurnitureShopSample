from django.urls import path
from .views import *

# app_name = 'shop'

urlpatterns = [
    path('shop', shop_main, name='shop'),
    path('<slug:category_slug>', shop_main, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('news', our_news, name='news'),
    path('<slug:post>', news_detail, name='news_detail'),
    path('', home_page, name='home_page'),
    path('about_us/', about_us, name='about_us'),
    path('contact_us/', contact_us, name='contact_us'),
    path('contact', contact, name='contact'),
]
