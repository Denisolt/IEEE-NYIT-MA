from django.conf.urls import url, include
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project', views.project, name='project'),
    url(r'^completed', views.completed, name='completed'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^admin/', include(admin.site.urls)),

]
