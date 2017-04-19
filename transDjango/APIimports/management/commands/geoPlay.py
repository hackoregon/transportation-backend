from django.core.management.base import BaseCommand
from APIimports.models import Feature, AddressGeocode
from django.core.cache import cache, caches
import networkx as nx
from django.contrib.gis.db.models.functions import Distance
import sys
from APIimports import models



class Command(BaseCommand):
    help = 'Pre-build as much as possible for the conflict views'

    def handle(self, *args, **options):

        o = models.Feature.objects.filter(pk__in=[47777, 47600])
        print('before', o)
        print('after', o.exclude(canonical_daterange__isempty=True))    


        # from psycopg2.extras import DateRange
        # import datetime

        # d1 = datetime.date(2016, 3, 15)
        # d2 = datetime.date(2016, 3, 20)
        # dr1 = DateRange(lower=d1, upper=d2)
        
        # d3 = datetime.date(2016, 4, 15)
        # d4 = datetime.date(2016, 4, 20)
        # dr2 = DateRange(lower=d3, upper=d4)
        # print(dr1, dr2)
        # print(dr2-dr1)
        # for n in models.Neighborhood.objects.all():
        #     adjacents = models.Neighborhood.objects.filter(geom__touches=n.geom)
        #     print(n.name, '----', list(adjacents.values('name')))


        # address = '1211 SW 5th Ave, Portland, OR'
        # #addresses = AddressGeocode.objects.using('geocoder').raw("SELECT g.rating, ST_X(g.geomout) As lon, ST_Y(g.geomout) As lat, (addy).address As stno, (addy).streetname As street, (addy).streettypeabbrev As styp, (addy).location As city, (addy).stateabbrev As st,(addy).zip FROM geocode(%s) As g;", [address])
        # geoaddy = AddressGeocode.objects.using('geocoder').raw("SELECT g.rating, ST_X(g.geomout) AS lon, ST_Y(g.geomout) AS lat, pprint_addy(addy) AS address FROM geocode(%s) as g LIMIT 1", [address])[0]
        # print(geoaddy.address)
        # # for obj in geoaddy:
        #     print('{o.rating} {o.lat} {o.lon} {o.address}'.format(o=obj))
        
        # f1 = Feature.objects.get(pk=1)
        # f2 = Feature.objects.get(pk=2)
        
        # g = nx.Graph()
        # g.add_nodes_from([f1, f2])
        # g.add_edge(f1, f2, distance=3)
        # g.add_edge(f1, f2, time=3)
        # print(g.edges(data=True))
        # sys.exit()

        # g = nx.Graph()
        # n1 = "this"
        # n2 = "that"
        # g.add_nodes_from([n1, n2])
        # g.add_edge(n1, n2, weight='first')
        # g.add_nodes_from([n2, n1])
        # g.add_edge(n1, n2, weight2='second')
        # for e in g.edges(data=True):
        #     print(e)
        # sys.exit()


        # featureGraph = nx.Graph()
        # features = Feature.objects.all()
        # polyIDs = [f.id for f in features if 'POLYGON' in str(f.geom).upper()]
        # featuresNoPolys = Feature.objects.exclude(id__in=polyIDs)

        # stopper = 0
        # for idx, f1 in enumerate(featuresNoPolys):
        #     print('idx', idx)
        #     for f2 in features[idx+1:]:
        #         success = addNodes(featureGraph, f1, f2)
        #         if success:
        #             stopper += 1
        #         if stopper > 5:
        #             break
        #     if idx > 10:
        #         break
    
        # print('nodecount', nx.number_of_nodes(featureGraph))
        # print('edgecount', nx.number_of_edges(featureGraph))

        # datedFeatureIds = [f.id for f in featureGraph.nodes()]
        # datedFeatures = Feature.objects.filter(pk__in=datedFeatureIds)

        # for e in featureGraph.edges(data=True):
        #     print(e)
        
        
        # counter = 0
        # fset = set()
        # for f1 in featureGraph.nodes():
        #     counter += 1
        #     print('counter', counter)
        #     for f2 in datedFeatures.exclude(pk=f1.id).annotate(distance=Distance('geom', f1.geom)):
        #         # print(f1.id, f2.id)
        #         # print(f1.canonical_daterange, f2.canonical_daterange)
        #         if featureGraph.has_edge(f1, f2):
        #             featureGraph.add_edge(f1, f2, distance=f2.distance.m)

                
        # print('nodecount', nx.number_of_nodes(featureGraph))
        # print('edgecount', nx.number_of_edges(featureGraph))

        # for e in featureGraph.edges(data=True):
        #     print(e)

        # print('nodecount', nx.number_of_nodes(featureGraph))
        # print('edgecount', nx.number_of_edges(featureGraph))

        # sys.exit()

        # sys.exit()
        # print(f1.geom, '\n++++++++++')
        # print(f2.geom, '\n=============')
        # print(f1.geom.distance(f2.geom))
        # print('\n*************************\n')
        # print(f1.geom.transform(4326, clone=True).distance(f2.geom.transform(4326, clone=True)))
        # print('\n*************************\n')
        # d = Distance(f1.geom, f2.geom)
        # print('\nd=\n', d)
        # print('\n^^^^^^^^^^^^^^^^^^^^^^^^^\n')
        # sys.exit()

        #featuresExcl = Feature.objects.exclude(geom__icontains='Polygon').all()
        #featuresAll = Feature.objects.all()
        #print('all count, excl count', featuresAll.count(), featuresExcl.count())

        # featureGraph = cache.get('featureGraph')    
        # for n in featureGraph.nodes():
        #     for n2 in featureGraph[n]:
        #         attrib = featureGraph.get_edge_data(n, n2)
        #         print('n1id, n2id', n.id, n2.id)
        #         print('t, d', attrib['time'], attrib['dist'].m)
                
        # sys.exit()
        
        # features = Feature.objects.all()
        # polyCount = 0        
        # for idx, f1 in enumerate(features):
        #     if 'Polygon' in str(f1.geom) or 'POLYGON' in str(f1.geom):
        #         polyCount += 1
        #     #print(f1.geom)
        #     # if 'Polygon' in str(f1.geom) or 'POLYGON' in str(f1.geom):
        #     #     continue
        #     # print('idx', idx)
        #     # for f2 in features[idx+1:]:
                
        #     #     # if not featureGraph.has_node(f1) or f2 not in featureGraph.neighbors(f1):
        #     #     #     addNodes(featureGraph, f1, f2)
        #     # if idx > 10:
        #     #     break
        # print('polycount', polyCount)