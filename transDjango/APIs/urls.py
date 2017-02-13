from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PointView.as_view(), name='points'),
]