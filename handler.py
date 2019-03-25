import json

from pipeline import Pipeline, events, functions
from sat_czml import Satellite, Constellation

class SatelliteCzmlAPI(Pipeline):
    def __init__(self):
        super().__init__()

    @functions.memory(3008)
    @events.http(path='landsat', method='post', cors='true')
    def landsat(self, event, context):
        sat_names = ['Landsat 7', 'Landsat 8']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 185000,
                 'swath_color': [65,171,93,125],
                 'track_color': [65,171,93,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='sentinel1', method='post', cors='true')
    def sentinel1(self, event, context):
        sat_names = ['Sentinel-1A', 'Sentinel-1B']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 250000,
                 'swath_color': [223,101,176,125],
                 'track_color': [223,101,176,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='sentinel2', method='post', cors='true')
    def sentinel2(self, event, context):
        sat_names = ['Sentinel-2A', 'Sentinel-2B']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 290000,
                 'swath_color': [106,81,163,125],
                 'track_color': [106,81,163,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response
    @functions.memory(3008)
    @events.http(path='cbers', method='post', cors='true')
    def cbers(self, event, context):
        sat_names = ['CBERS 4']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 120000,
                 'swath_color': [239,59,44,125],
                 'track_color': [239,59,44,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='skysat', method='post', cors='true')
    def skysat(self, event, context):
        sat_names = ['Skysat-C{}'.format(x) for x in range(1, 12)] + ['Skysat-1', 'Skysat-2']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 8000,
                 'swath_color': [66,146,198,125],
                 'track_color': [66,146,198,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='pleiades', method='post', cors='true')
    def pleiades(self, event, context):
        sat_names = ['Pleiades 1a', 'Pleiades 1b']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 20000,
                 'swath_color': [254,196,79,125],
                 'track_color': [254,196,79,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='rapideye', method='post', cors='true')
    def rapideye(self, event, context):
        sat_names = ['RapidEye 1', 'RapidEye 2', 'RapidEye 3', 'RapidEye 4', 'RapidEye 5']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 77000,
                 'swath_color': [140,81,10,125],
                 'track_color': [140,81,10,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='terrasar', method='post', cors='true')
    def terrasar(self, event, context):
        args = [
            {'name': 'TerraSAR-X',
             'speed': event['speed'],
             'orbit_count': event['orbit_count'],
             'swath_width': 260000,
             'swath_color': [115,115,115,125],
             'track_color': [115,115,115,255],
             },
            {'name': 'TanDEM-X',
             'speed': event['speed'],
             'orbit_count': event['orbit_count'],
             'swath_width': 30000,
             'swath_color': [115, 115, 115, 125],
             'track_color': [115, 115, 115, 255],
             }
        ]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

    @functions.memory(3008)
    @events.http(path='cosmoskymed', method='post', cors='true')
    def cosmoskymed(self, event, context):
        sat_names = ['Cosmo-Skymed 1', 'Cosmo-Skymed 2', 'Cosmo-Skymed 3', 'Cosmo-Skymed 4']
        args = [{'name': x,
                 'speed': event['speed'],
                 'orbit_count': event['orbit_count'],
                 'swath_width': 200000,
                 'swath_color': [152,0,67,125],
                 'track_color': [152,0,67,255],
                 } for x in sat_names]

        response = {
            'statusCode': 200,
            'body': json.dumps(Constellation.load(args).execute())
        }

        return response

pipeline = SatelliteCzmlAPI()


"""Lambda handlers"""

landsat = pipeline.landsat
sentinel1 = pipeline.sentinel1
sentinel2 = pipeline.sentinel2
cbers = pipeline.cbers
skysat = pipeline.skysat
pleiades = pipeline.pleiades
rapideye = pipeline.rapideye
terrasar = pipeline.terrasar
cosmoskymed = pipeline.cosmoskymed


"""Deploy pipeline"""


def deploy():
    pipeline.deploy()
