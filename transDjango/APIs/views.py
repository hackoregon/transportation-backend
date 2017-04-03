from APIimports.models import Point, Line, Polygon
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PointSerializer, LineSerializer, PolygonSerializer
from rest_framework import authentication, permissions
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from django.core.cache import cache

# Create your views here.


class PointView(generics.ListCreateAPIView):

    model = Point
    serializer_class = PointSerializer
    queryset = Point.objects.prefetch_related('sourceRef')


class LineView(generics.ListCreateAPIView):

    model = Line
    serializer_class = LineSerializer
    queryset = Line.objects.prefetch_related('sourceRef')


class PolygonView(generics.ListCreateAPIView):
    model = Polygon
    serializer_class = PolygonSerializer
    queryset = Polygon.objects.prefetch_related('sourceRef')


class ConflictView(generics.ListCreateAPIView):
    serializer_class = PointSerializer

    def get_queryset(self, minDist=14):
        # tstart = datetime.datetime.now() 
        # global collisionGraph
        # collisionGraph = nx.Graph()
        # points = Point.objects.prefetch_related('sourceRef')
        # # pnt = GEOSGeometry('POINT(-96.876369 29.905320)', srid=4326)
        # # pointsVsPoints = Point.objects.filter(geom__distance_lte(pnt, D(m=200)))
        # # overlapSet = set()
        # for idx, point in enumerate(points):
        #     p1pk = 'point' + str(point.pk)
        #     # print('===================')
        #     # print(point.dateRange)

        #     for cPoint in points[idx+1:]:
        #         p2pk = 'point' + str(cPoint.pk)
        #         if not collisionGraph.has_node(p1pk) or p2pk not in collisionGraph.neighbors(p1pk):
        #             self.addNodes(point, cPoint, p1pk, p2pk)

        #     # overlapSet |= set(pointsVsPoints)
        #     # print(pointsVsPoints)

        # # print(overlapSet)
        # pointsVsPoints = Point.objects.filter(geom__distance_lte=(point.geom, D(m=200)))

        # print('connected count', str(nx.connected_components(collisionGraph)))
        
        collisionGraph = cache.get('dateGraph')
        pointset = set()
        for u,v,d in collisionGraph.edges(data=True):
            if d['weight'] <= minDist:
                # print (u, v, d)
                if d['weight'] < minDist:
                    pointset = {u, v} | pointset
                    
        return pointset

    # def addNodes(self, point, cPoint, p1pk, p2pk):
    #     ps = point.dateRange.lower
    #     pe = point.dateRange.upper
    #     cs = cPoint.dateRange.lower
    #     ce = cPoint.dateRange.upper
    #     if all([ps, pe, cs, ce]):

    #         distance = (max(ps, cs) - min(pe, ce)).days
    #         if distance < 0:
    #             distance = 0
    #         # print('dist=', distance)
    #         collisionGraph.add_nodes_from([p1pk, p2pk])
    #         collisionGraph.add_edge(point, cPoint, weight=distance)
