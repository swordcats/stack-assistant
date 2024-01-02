import sqlite3

class Connection:
    def __init__(self, database_name: str):
        self.connection = sqlite3.connect(database_name)

    def execute_statement(self, statement: str):
        self.connection.execute(statement)


__all__ = [Connection.__name__]