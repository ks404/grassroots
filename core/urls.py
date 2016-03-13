from django.conf.urls import url, include

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]
