from .models import Point, Line, Polygon
from django.core.cache import cache, caches
import networkx as nx


def getAllDateDistances(minDist=14):

    collisionGraph = nx.Graph()
    points = Point.objects.prefetch_related('sourceRef')
    # pnt = GEOSGeometry('POINT(-96.876369 29.905320)', srid=4326)
    # pointsVsPoints = Point.objects.filter(geom__distance_lte(pnt, D(m=200)))
    # overlapSet = set()
    for idx, point in enumerate(points):
        p1pk = 'point' + str(point.pk)
        # print('===================')
        # print(point.dateRange)

        for cPoint in points[idx+1:]:
            p2pk = 'point' + str(cPoint.pk)
            if not collisionGraph.has_node(p1pk) or p2pk not in collisionGraph.neighbors(p1pk):
                addNodes(collisionGraph, point, cPoint, p1pk, p2pk)
    #print('cg pre', collisionGraph.nodes())
    cache.set('dateGraph', collisionGraph, None)
    #print('all caches', caches.all())
    #myc = caches.all()
    #print('mydir', dir(myc))
    cg = cache.get('dateGraph')
    print('check', cache.get('dateGraph').nodes())

def addNodes(graph, point, cPoint, p1pk, p2pk):
    ps = point.dateRange.lower
    pe = point.dateRange.upper
    cs = cPoint.dateRange.lower
    ce = cPoint.dateRange.upper
    if all([ps, pe, cs, ce]):

        distance = (max(ps, cs) - min(pe, ce)).days
        if distance < 0:
            distance = 0
        # print('dist=', distance)
        graph.add_nodes_from([p1pk, p2pk])
        graph.add_edge(point, cPoint, weight=distance)
