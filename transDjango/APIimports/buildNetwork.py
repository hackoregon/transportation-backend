from .models import Point, Line, Polygon
from django.core.cache import cache, caches
import networkx as nx


def getAllDateDistances(minDist=14):

    collisionGraph = nx.Graph()
    points = Point.objects.prefetch_related('sourceRef')
    lines = Line.objects.prefetch_related('sourceRef')
    print('pointslen', len(points))
    for idx, p1 in enumerate(points):
        print('idx pvp', idx)
        for p2 in points[idx+1:]:
            if not collisionGraph.has_node(p1) or p2 not in collisionGraph.neighbors(p1):
                addNodes(collisionGraph, p1, p2)

    for idx, point in enumerate(points):
        print('idx pvl', idx)
        for line in lines:
            addNodes(collisionGraph, point, line)

    for idx, l1 in enumerate(lines):
        print('idx lvl', idx)
        for l2 in lines[idx+1:]:
            if not collisionGraph.has_node(l1) or l2 not in collisionGraph.neighbors(l1):
                addNodes(collisionGraph, l1, l2)

    print('nodecount', nx.number_of_nodes(collisionGraph))
    print('edgecount', nx.number_of_edges(collisionGraph))
    cache.set('dateGraph', collisionGraph, None)


def addNodes(graph, obj1, obj2):
    obj1s = obj1.dateRange.lower
    obj1e = obj1.dateRange.upper
    obj2s = obj2.dateRange.lower
    obj2e = obj2.dateRange.upper
    if all([obj1s, obj1e, obj2s, obj2e]):

        distance = (max(obj1s, obj2s) - min(obj1e, obj2e)).days
        if distance < 0:
            distance = 0
        # print('dist=', distance)
        graph.add_nodes_from([obj1, obj2])
        graph.add_edge(obj1, obj2, weight=distance)
