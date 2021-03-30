from usdaXLSX import getUSDALinks, downloadXLSX, readXLSX
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)


class Fruits(Resource):
    def get(self, type="empty"):
        data =  readXLSX('data/fruits')
        return {'data': data}, 200  # return data and 200 OK code
    pass
class Vegetables(Resource):
    def get(self):
        data =  readXLSX('data/vegetables')
        return {'data': data}, 200  # return data and 200 OK code
    pass
class UpdatePrices(Resource):
    def get(self):
        getUSDALinks(downloadXLSX)
        return {'data': "update complete!"}, 200  # return data and 200 OK code
    pass
    
    
api.add_resource(Fruits, '/fruits','/fruits/<type>')  # '/Fruits entry point
api.add_resource(Vegetables, '/vegetables')  # '/vegetables entry point
api.add_resource(UpdatePrices, '/updatePrices')  # '/updarePrices entry point

if __name__ == '__main__':
    app.run()  # run our Flask app