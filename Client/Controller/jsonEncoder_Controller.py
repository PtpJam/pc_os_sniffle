import json

from Client.Model.userNetworkData import userNetworkData


class jsonEncoder(json.JSONEncoder):
    def toJson(self, obj):
        if isinstance(obj, userNetworkData):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)