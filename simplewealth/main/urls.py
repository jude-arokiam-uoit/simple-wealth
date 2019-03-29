from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', LoginView.as_view(template_name='main/home.html'),name="login"),
]