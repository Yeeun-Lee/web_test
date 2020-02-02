from django.conf.urls import url
from django.conf import settings
from . import views
# from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^logout/$',views.logout,name = 'logout'),
	url(r'^login/$',views.login, name = 'login'),
	url(r'^signup/$', views.signup, name ="signup")
]