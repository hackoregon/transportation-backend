from .models import Feature, API_element
from django.core.cache import cache, caches
import networkx as nx
from django.contrib.gis.db.models.functions import Distance
from psycopg2.extras import DateRange
from .constants import API_META, CSV_META, GEOJSON_META
import sys


def buildGraphs():


    featureGraph = nx.Graph()
    
    # There are some polygon sources that we want to ignore
    excludeSourceRefs = list()
    sourceDict = {}
    sourceDict.update(API_META)
    sourceDict.update(CSV_META)
    sourceDict.update(GEOJSON_META)
    for sourceName in sourceDict:
        if not sourceDict[sourceName]['forConflict']:
            excludeSourceRefs.append(API_element.objects.get(api_name=sourceName).id)
    
    excludeStatuses = ['COMPLETED', 'COMPLETED', 'REQUESTED', 'COMPLETE', 'DENIED', 'CANCELED']

    
    
    filteredFeatures = Feature.objects\
        .exclude(canonical_daterange=None)\
        .exclude(canonical_daterange__isempty=True)\
        .exclude(neighborhood__isnull=True)\
        .exclude(source_ref__in=excludeSourceRefs)\
        .exclude(canonical_status__in=excludeStatuses)\
        .filter(canonical_daterange__overlap=DateRange(lower='2015-01-01', upper='2020-01-01'))
        
    # print('filteredFeatures count', filteredFeatures.count())
    
    for idx, f1 in enumerate(filteredFeatures):
        # print('idx', idx)
        for f2 in filteredFeatures[idx+1:]:
            if f1.id == f2.id:
                continue
        
            daysApart = getDayDiff(f1, f2)
            featureGraph.add_nodes_from([f1.id, f2.id])
            featureGraph.add_edge(f1.id, f2.id, {'daysApart':daysApart})
            
        # if idx > 10:
        #     break

    # print('nodecount', nx.number_of_nodes(featureGraph))
    # print('edgecount', nx.number_of_edges(featureGraph))
    
    datedFeatureIDs = [f for f in featureGraph.nodes()]
    datedFeatures = Feature.objects.filter(pk__in=datedFeatureIDs)

    # for e in featureGraph.edges(data=True):
    #     print(e)

    counter = 0
    # print(datedFeatures.get(pk=46907))
    # print(featureGraph[46907])
    # print(featureGraph.neighbors(46907))
    
    for f1 in datedFeatures:
        
        connected = featureGraph.neighbors(f1.id)
        cids = [f for f in connected]
        connectedFeatures = Feature.objects.filter(pk__in=cids)

        counter += 1
        # print('counter: {} of {}'.format(counter, datedFeatures.count()))
        for f2 in connectedFeatures.annotate(distance=Distance('geom', f1.geom)):
            # print(f1.id, f2.id)
            # print(f1.canonical_daterange, f2.canonical_daterange)            
            featureGraph.add_edge(f1.id, f2.id, distance=f2.distance.m)
            if f2.distance.m < 100.0:
                print(f2.distance, "|", f1, "|", f2)

    print('nodecount', nx.number_of_nodes(featureGraph))
    print('edgecount', nx.number_of_edges(featureGraph))

    cache.set('featureGraph', featureGraph, None)


def getDayDiff(obj1, obj2):
    obj1s = obj1.canonical_daterange.lower
    obj1e = obj1.canonical_daterange.upper
    obj2s = obj2.canonical_daterange.lower
    obj2e = obj2.canonical_daterange.upper

    dayDist = (max(obj1s, obj2s) - min(obj1e, obj2e)).days
    if dayDist < 0:
        dayDist = 0
    
    return dayDist

