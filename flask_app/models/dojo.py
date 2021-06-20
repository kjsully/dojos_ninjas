from ..config.mysqlconnection import connectToMySQL

from ..models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []



    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []

        for row in results:
            dojos.append(Dojo(row))

        print(dojos)
        return dojos


    @classmethod
    def create(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        
        dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        
        print(dojo_id)
        return dojo_id


    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        dojo = Dojo(results[0])

        for row in results:
            dojo.ninjas.append(Ninja(row))
        
        return dojo