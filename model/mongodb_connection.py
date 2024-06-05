from pymongo import MongoClient


class Mongodb:

    def __init__(self, database) -> None:
        
        self.database = database
        self.str_route18 = 'mongodb://localhost:27018/'
        self.str_route19 = 'mongodb://localhost:27019/'
        self.str_route20 = 'mongodb://localhost:27020/'

        
    def mongodbroute18(self):
        client = MongoClient('mongodb://localhost:27018/')
        return client[self.database]


    def mongodbroute19(self):
        client = MongoClient('mongodb://localhost:27019/')
        return client[self.database]
    

    def mongodbroute20(self):
        client = MongoClient('mongodb://localhost:27020/')
        return client[self.database]