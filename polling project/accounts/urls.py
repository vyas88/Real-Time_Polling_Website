from django.urls import path
from . import views
app_name = "accounts"
urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('about-us/', views.about_us, name='about_us'),
    path('our-services/', views.our_services, name='our_services'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
]

