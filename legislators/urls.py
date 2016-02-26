from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^api/$', views.FedCongressListView.as_view()),
    url('^api/zipcode/(?P<zipcode>[0-9]{5})/$', views.federal_zip_lookup)
]
