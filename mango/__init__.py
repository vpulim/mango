from django.conf import settings
from pymongo import Connection
import pymongo.errors

OperationFailure = pymongo.errors.OperationFailure
_connection = Connection(settings.MONGODB_HOST, settings.MONGODB_PORT)
database = _connection[settings.MONGODB_NAME] if _connection else None

class Model(object):

    valid_fields = []

    def __init__(self, result, collection):
        object.__setattr__(self, 'id', result['_id'])
        object.__setattr__(self, 'fields', result)
        object.__setattr__(self, 'collection', collection)

    def __getattr__(self, attr):
        try:
            fields = self.__dict__['fields']
            return fields[attr]
        except KeyError:
            return None

    def __setattr__(self, attr, value):
        if attr in self.__class__.__dict__['valid_fields']:
            fields = self.__dict__['fields']
            fields[attr] = value
        else:
            self.__dict__[attr] = value

    def save(self):
        fields = self.__dict__['fields']
        collection = self.__dict__['collection']
        collection.save(fields, safe=True)
