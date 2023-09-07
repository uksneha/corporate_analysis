import psycopg2 as psycopg2
from variables.error_list import *


class Database:
    def __init__(self):
        self.dbname = "corporate_data"
        self.user = "postgres"
        self.password = "123qwe"
        self.host = "localhost"
        self.port = "5432"
        self.conn = None
        self.cursor = None

    def get_connection(self, cursor_factory=None):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                    cursor_factory=cursor_factory
                )
            except Exception as e:
                self.conn = None
                print(e)

        return self.conn

    def execute(self, query, params=None):
        if self.cursor is None:
            self.cursor = self.get_connection().cursor()
        self.cursor.execute(query, params)

    def commit(self):
        if self.cursor is not None:
            self.conn.commit()

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        self.cursor = None
        self.conn = None

    @staticmethod
    def exec_sp_return_one(conn, procedure_name, value_list):
        with conn.cursor() as cur:
            try:
                cur.callproc(
                    procedure_name,
                    value_list
                )
                results = cur.fetchone()
                conn.commit()
                return [results, 1]
            except Exception as e:
                print("Database Connection Error -->\n" + str(e))
                conn.rollback()
                return [databaseError(str(e)), 0]

    @staticmethod
    def exec_stored_procedure(conn, procedure_name, value_list):
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.callproc(
                        procedure_name,
                        value_list
                    )
                    results = cursor.fetchall()
                    conn.commit()
                    return [results, 1]
                except Exception as e:
                    print("Database Error -->\n" + str(e))
                    conn.rollback()
                    return [databaseError(str(e)), 0]
        except Exception as e:
            print("Database Connection Error -->\n" + str(e))
            return [databaseError(str(e)), 0]
