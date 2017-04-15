from .models import Feature, API_element
from django.core.cache import cache, caches
import networkx as nx
from django.contrib.gis.db.models.functions import Distance
from .constants import API_META, CSV_META, GEOJSON_META
import sys


def buildGraphs():


    featureGraph = nx.Graph()

    
    conflictSourceIDs = []

    z = API_element.objects.values_list('api_name')
    print(z)
    sourceNames = list(API_META.keys()) + list(CSV_META.keys()) + list(GEOJSON_META.keys())
    sourceDict = {}
    sourceDict.update(API_META)
    sourceDict.update(CSV_META)
    sourceDict.update(GEOJSON_META)
    for sourceName in sourceDict:
        if sourceDict[sourceName]['forConflict']:
            conflictSourceIDs.append(API_element.objects.get(api_name=sourceName).id)
            

    print('\n'.join(conflictSourceIDs))
    sys.exit()

    features = Feature.objects.all()
    polyIDs = [f.id for f in features if 'POLYGON' in str(f.geom).upper()]
    featuresNoPolys = Feature.objects.exclude(id__in=polyIDs)

    for idx, f1 in enumerate(featuresNoPolys):
        print('idx', idx)
        for f2 in features[idx+1:]:
            if f1.id == f2.id:
                continue
            addNodes(featureGraph, f1, f2)
            
        # if idx > 10:
        #     break

    print('nodecount', nx.number_of_nodes(featureGraph))
    print('edgecount', nx.number_of_edges(featureGraph))

    datedFeatureIds = [f.id for f in featureGraph.nodes()]
    datedFeatures = Feature.objects.filter(pk__in=datedFeatureIds)

    # for e in featureGraph.edges(data=True):
    #     print(e)

    counter = 0
    for f1 in datedFeatures:

        connected = featureGraph.neighbors(f1)
        cids = [f.id for f in connected]
        # print(cids)
        connectedFeatures = Feature.objects.filter(pk__in=cids)

        counter += 1
        print('counter', counter)
        for f2 in connectedFeatures.annotate(distance=Distance('geom', f1.geom)):
            # print(f1.id, f2.id)
            # print(f1.canonical_daterange, f2.canonical_daterange)            
            featureGraph.add_edge(f1, f2, distance=f2.distance.m)

    print('nodecount', nx.number_of_nodes(featureGraph))
    print('edgecount', nx.number_of_edges(featureGraph))

    # for e in featureGraph.edges(data=True):
    #     print(e)

    print('nodecount', nx.number_of_nodes(featureGraph))
    print('edgecount', nx.number_of_edges(featureGraph))

    cache.set('featureGraph', featureGraph, None)


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
        graph.add_edge(obj1, obj2, daysApart=dayDist)
        return True
    else: 
        return False

