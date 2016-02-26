from django.conf.urls import url, include

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^legislators/', include('legislators.urls')),
]
