import json
import psycopg2


class Connection:

    def __init__(self, location: str = "./config/database.json"):
        self.location = location
        self.connection = self.start()

    def start(self):
        with open(self.location) as json_file:
            return self.create_connection(json.load(json_file)["postgres"])

    def create_connection(self, data):
        return psycopg2.connect(database=data["dns"]["database"], user=data["connect"]["user"], password=data["connect"]["password"], host=data["dns"]["host"], port=data["dns"]["port"])

    def close(self):
        self.connection.close()

    def exec(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = [row for row in cursor]
        cursor.close()
        return data

    '''def exec(self, sql):
        #cursor = self.connection.cursor()
        #cursor.execute(sql)
        #data = [row for row in cursor]
        #cursor.close()
        #return data

    def create_dns(self, data):
        #return cx_Oracle.makedsn(host=data["host"], port=data["port"], sid=data["sid"])

    def create_connection(self, data):
        #self.connection = cx_Oracle.connect(user=data["connect"]["user"], password=data["connect"]
        #                                    ["password"], encoding="UTF-8", nencoding="UTF-8", dsn=self.create_dns(data["dns"]))

    def close(self):
        #self.connection.close()
'''
