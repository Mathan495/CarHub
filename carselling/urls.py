from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about us/', views.about_page, name="about"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register_Page, name="register"),
    path('collections/', views.collections_page, name="collections"),
    path('collections/<str:name>', views.collections_view, name="collections"),
    path('car_details/<str:cname>/<str:pname>', views.cars_details, name="car_details"),
    path('contact/', views.contact_page, name="contact"),
    # path('fav/', views.fav_page, name="fav"),
]
