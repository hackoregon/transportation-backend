from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^points/', views.PointView.as_view(), name='points'),
    url(r'^lines/', views.LineView.as_view(), name='lines'),
    url(r'^polygons/', views.PolygonView.as_view(), name='polygons'),
    url(r'^conflicts/', views.ConflictView.as_view(), name='conflicts'),
]