from data_manager import DataManager

def query_database():
    data_manager = DataManager('example.db', 'students')
    results = data_manager.query_data()
    for row in results:
        print(row)

if __name__ == "__main__":
    query_database()