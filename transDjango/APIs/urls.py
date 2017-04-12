from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^features/$', views.FeatureView.as_view(), name='features'),
    url(r'^conflicts/$', views.ConflictView.as_view(), name='conflicts'),
    url(r'^nearby/$', views.NearbyProjects.as_view(), name='nearby'),
]