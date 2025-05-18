from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("MySQL connection")

class MongoDB(Database):
    def connect(self):
        print("MongoDB connection")

# Usage
databases = [MySQL(), MongoDB()]
for db in databases:
    db.connect()  # Output: MySQL connection / MongoDB connection