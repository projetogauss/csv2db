#Before install in your env the lib psycopg2 using pip.
#pip install psycopg2
import psycopg2

class Connectionpg():
    def createconnection():
        try:
            conn = psycopg2.connect(user="user",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="database")
        except (psycopg2.Error) as error:
            print(error)
        return conn