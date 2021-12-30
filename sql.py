import psycopg2
from config import config

class SQL:

    @staticmethod
    def read_single(query):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # conn.autocommit = True
            # create a cursor
            cur = conn.cursor()
            # execute a statement
            cur.execute(query)
            # display the PostgreSQL database server version
            return cur.fetchone()
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def execute(query, parameters):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # conn.autocommit = True
            # create a cursor
            cur = conn.cursor()
            cur.execute(query, parameters)
            conn.commit()
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

