from psycopg2 import pool
from pathlib import Path
from datetime import date
from subprocess import Popen


class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1, 2, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def return_all_connection(cls):
        cls.__connection_pool.closeall()


class ConnectionPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            self.cursor.close()
            self.connection.commit()
        else:
            self.connection.rollback()
        return Database.return_connection(self.connection)


class DatabaseMaintenance:
    def __init__(self, dbname, postgres_version=11):
        # noinspection SpellCheckingInspection
        self.postgres_dir = Path(f"C:/Program Files/PostgreSQL/{postgres_version}/bin/")
        self.dbname = dbname

    def create_backup(self, backup_path, host='localhost', user='postgres', port=5432):
        try:
            filename = f'{str(date.today())}_{self.dbname}.tar'
            save_dir = Path(backup_path) / filename

            process = Popen(['pg_dump', '-h', host, '-U', user, '-w', '-p', str(port), '-F', 't',
                             '-f', str(save_dir), '-d', self.dbname], cwd=self.postgres_dir, shell=True)
            process.wait()
            result = process.poll()
            return result

        except Exception as error:
            return str(error)

    def create_db(self, host='localhost', user='postgres', port=5432):
        try:
            process = Popen(['createdb', '-h', host, '-U', user, '-w', '-p', str(port), '-e', self.dbname],
                            cwd=self.postgres_dir, shell=True)
            process.wait()
            result = process.poll()
            return result
        except Exception as error:
            return str(error)

    def restore_db(self, restore_file, host='localhost', user='postgres', port=5432, postgres_version=11):
        try:
            restore_file = f'D:/Documents/IT Files/Cantina/Staff Ordering System/classes/{restore_file}'
            process = Popen(['pg_restore', '-h', host, '-U', user, '-w', '-p', str(port), '-d',
                             self.dbname, restore_file],
                            cwd=self.postgres_dir, shell=True)
            process.wait()
            result = process.poll()
            return result
        except Exception as error:
            return str(error)


if __name__ == '__main__':
    path = 'D:/Documents/IT Files/Cantina/Staff Ordering System/backup'
    db_name = 'COMPSCI_IA'
    db_host = 'localhost'
    db_user = 'postgres'
    db_port = 5434
    maintenance = DatabaseMaintenance()
    # maintenance.create_backup(path, db_name, db_host, db_user, db_port)
    maintenance.create_db('Testing2', db_host, db_user, db_port)
    maintenance.restore_db('Testing2', '2020-03-11_cantina.tar', db_host, db_user, db_port)