from django.conf.urls import url, include

from legislators import views

urlpatterns = [
    url(r'^$', views.enter_zip, name='enter-zip'),
    url(r'^legislators/zipcode/(?P<zipcode>[0-9]{5})/$', views.zip_detail, name='zip-detail'),
    url(r'^api/$', views.FedCongressListView.as_view()),
    url(r'^api/zipcode/(?P<zipcode>[0-9]{5})/$', views.federal_zip_lookup)
]
