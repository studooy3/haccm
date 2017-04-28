from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^base/$', views.BasePageView.as_view(), name='base'),
    url(r'^resource/$', views.ResourcePageView.as_view(), name='resource'),
    url(r'^event/$', views.EventPageView.as_view(), name='event'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^test/$', views.TestPageView.as_view(), name='test'),
    
]