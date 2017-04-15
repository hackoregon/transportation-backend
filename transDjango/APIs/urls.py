from django.conf.urls import url

from . import views

schema_view = get_swagger_view(title='Team Transportation API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^features/$', views.FeatureView.as_view(), name='features'),
    url(r'^features/(?P<pk>[0-9]+)/$', views.FeatureDetailView.as_view()),
    url(r'^conflicts/$', views.ConflictView.as_view(), name='conflicts'),
    url(r'^nearby/$', views.NearbyProjects.as_view(), name='nearby'),
]
