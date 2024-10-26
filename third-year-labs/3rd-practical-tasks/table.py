from database import Database


class Table:
    def __init__(self, db_name, table_name, schema):
        self.db = Database(db_name)
        self.table_name = table_name
        self.schema = schema

    def create_table(self):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ({self.schema})")
        self.db.connection.commit()
        self.db.disconnect()
