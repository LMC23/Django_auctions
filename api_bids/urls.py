from django.urls import path
from . import views

from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('category', views.CategoryList.as_view()),
    path('auction', views.AuctionList.as_view()),
    path('login', auth_views.obtain_auth_token),
    path('auction/<int:pk>', views.AuctionDetail.as_view())
]