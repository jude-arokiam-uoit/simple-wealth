from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', LoginView.as_view(template_name='main/home.html'),name="login"),
    path('accounts/profile/', views.dash,name="dash"),
    path('accounts/profile/buy_sell/',views.buy_sell,name="buy_sell"),
]