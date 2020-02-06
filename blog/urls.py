from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Example : /
    url(r'^$', views.PostLV.as_view(), name = 'post-list'),
    # Example : /post/django-example
    # url(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name = 'post_detail'),
    # Example : /post/django-example
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post-detail'),
# path('<int:blog_id>', views.detail, name='post-detail'),
    path('new/', views.new, name='new'),
    # path('posts/', views.post_lists, name = 'post-list'),
    path('create/', views.create, name='create'),
    path('notice/', views.NoticeLV.as_view(), name = 'notice'),
    url(r'^notice/(?P<slug>[-\w]+)/$', views.NoticeDV.as_view(), name='notice-detail'),
    path('about/', views.about, name='about'),
    path('competition/', views.CompetitionLV.as_view(), name='competition'),
    path('submission/', views.sub_page, name = 'sub_page'),
    path('uploadfile/',views.new_submission, name = 'submit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)