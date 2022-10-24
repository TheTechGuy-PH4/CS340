from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:47544' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert != 0:
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            ds = self.database.animals.find(data, {"_id":False})
            return ds
        else:
            raise Exception("Data is not in Database")
            
# Create method to implement the U in CRUD.
    def update(self, data, data2):
        if data is not None:
            self.database.animals.update(data, data2)
            print(json.dumps(data))
        else:
            raise Exception("Data is not in Database")
            
        
# Create method to imlement the D in CRUD.
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)
            print(json.dumps(data))
        else:
            delEx = "Data is not in Database"
            return delEx
            
            