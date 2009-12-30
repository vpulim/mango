from django.conf import settings
from pymongo import Connection
import pymongo.errors

OperationFailure = pymongo.errors.OperationFailure
_connection = Connection(settings.MONGODB_HOST, settings.MONGODB_PORT)
database = _connection[settings.MONGODB_NAME] if _connection else None

class Model(object):

    collection = None

    def __init__(self, result):
        self._fields = result

    def __getattr__(self, attr):
        try:
            return self._fields[attr]
        except KeyError:
            return None

    def __setattr__(self, attr, value):
        if attr in ['id', '_fields']:
            object.__setattr__(self, attr, value)
        else:
            self._fields[attr] = value

    def save(self):
        self._fields['_id'] = self.collection.save(self._fields, safe=True)
        
    def delete(self):
        self.collection.remove({'_id': self._fields.get('_id', None)})
        self.id = None

    def get_id(self):
        return self._fields.get('_id', None)

    def get_doc(self):
        return self._fields

    id = property(get_id)
    doc = property(get_doc)

    @classmethod
    def get(cls, spec):
        if cls.collection:
            result = cls.collection.find_one(spec)
            if result:
                return cls(result)
        return None
