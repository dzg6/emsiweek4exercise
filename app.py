from usdaXLSX import *
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse

# import ast
app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)


@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

class Fruits(Resource):
    # @cross_origin(origins="http://localhost:5000*")
    def get(self, todo_id="empty"):
        print(todo_id)
        # data = data.to_dict()  # convert dataframe to dictionary

        data =  readXLSX('data/fruits')
        return {'data': data}, 200  # return data and 200 OK code
    pass
class Vegetables(Resource):
    def get(self):
        # data = data.to_dict()  # convert dataframe to dictionary
        data =  readXLSX('data/vegetables')
        return {'data': data}, 200  # return data and 200 OK code
    pass
class UpdatePrices(Resource):
    def get(self):
        # data = data.to_dict()  # convert dataframe to dictionary
        getUSDALinks()
        return {'data': "update complete!"}, 200  # return data and 200 OK code
    pass
    
class Locations(Resource):
    # methods go here
    pass
    
api.add_resource(Fruits, '/fruits','/fruits/<todo_id>')  # '/Fruits entry point
api.add_resource(Vegetables, '/vegetables')  # '/Fruits entry point
api.add_resource(UpdatePrices, '/updatePrices')  # '/Fruits entry point
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app