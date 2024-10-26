from database import Database


class DataManager:
    def __init__(self, db_name, table_name):
        self.db = Database(db_name)
        self.table_name = table_name

    def insert_data(self, data):
        self.db.connect()
        cursor = self.db.connection.cursor()
        placeholders = ', '.join(['?'] * len(data))
        cursor.execute(
            f"INSERT INTO {self.table_name} VALUES ({placeholders})", data)
        self.db.connection.commit()
        self.db.disconnect()

    def update_data(self, set_clause, where_clause):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            f"UPDATE {self.table_name} SET {set_clause} WHERE {where_clause}")
        self.db.connection.commit()
        self.db.disconnect()

    def delete_data(self, where_clause):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE {where_clause}")
        self.db.connection.commit()
        self.db.disconnect()

    def query_data(self, select_clause='*', where_clause=''):
        self.db.connect()
        cursor = self.db.connection.cursor()
        query = f"SELECT {select_clause} FROM {self.table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"
        cursor.execute(query)
        results = cursor.fetchall()
        self.db.disconnect()
        return results
