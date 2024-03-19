from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index),
    # path('login/',TokenObtainPairView.as_view()),
    path('products/',views.Products.as_view()),
     path('cart/',views.Cart.as_view()),
 path('products/<int:id>',views.Products.as_view()),
     path('resgister/',views.register),
         path('get_all_images', views.getImages),
    path('upload_image/',views.APIViews.as_view()),
    path('login', views.MyTokenObtainPairView.as_view()),

]