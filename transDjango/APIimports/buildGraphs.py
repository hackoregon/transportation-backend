from .models import Feature
from django.core.cache import cache, caches
import networkx as nx
from django.contrib.gis.db.models.functions import Distance
import sys


def buildGraphs():
    
    f1 = Feature.objects.get(pk=10)
    f2 = Feature.objects.get(pk=655)
    print(f1.geom, '\n++++++++++')
    print(f2.geom, '\n=============')
    print(f1.geom.distance(f2.geom))
    print('\n*************************\n')
    print(f1.geom.transform(4326, clone=True).distance(f2.geom.transform(4326, clone=True)))
    print('\n*************************\n')
    d = Distance(f1.geom, f2.geom)
    print('\nd=\n', d)
    print('\n^^^^^^^^^^^^^^^^^^^^^^^^^\n')
    sys.exit()

    featureGraph = cache.get('featureGraph')    
    for n in featureGraph.nodes():
        for n2 in featureGraph[n]:
            attrib = featureGraph.get_edge_data(n, n2)
            print('n1id, n2id', n.id, n2.id)
            print('t, d', attrib['time'], attrib['dist'].m)
            
    # sys.exit()
        
    featureGraph = nx.Graph()
    features = Feature.objects.all()
    print('featureslen', len(features))
    for idx, f1 in enumerate(features):
        if 'Polygon' in str(f1.geom) or 'POLYGON' in str(f1.geom):
            continue
        print('idx', idx)
        for f2 in features[idx+1:]:
            if not featureGraph.has_node(f1) or f2 not in featureGraph.neighbors(f1):
                addNodes(featureGraph, f1, f2)
        if idx > 10:
            break

    print('nodecount', nx.number_of_nodes(featureGraph))
    print('edgecount', nx.number_of_edges(featureGraph))
    cache.set('featureGraph', featureGraph, None)
    # if distance:
    #     if not time:
    #         featureGraph = cache.get('featureGraph')
    #     for f in featureGraph.nodes():
    #         print('idx', idx)
    #         closeFeatures = Feature.objects.filter(geom__distance_lte=(f.geom, D(m=50)))
    #         pointSet = set(closeFeat) | pointSet



def addNodes(graph, obj1, obj2):
    obj1s = obj1.canonical_daterange.lower
    obj1e = obj1.canonical_daterange.upper
    obj2s = obj2.canonical_daterange.lower
    obj2e = obj2.canonical_daterange.upper
    if all([obj1s, obj1e, obj2s, obj2e]):

        dayDist = (max(obj1s, obj2s) - min(obj1e, obj2e)).days
        if dayDist < 0:
            dayDist = 0
        # print('dist=', distance)
        graph.add_nodes_from([obj1, obj2])
        graph.add_edge(obj1, obj2, time=dayDist)

