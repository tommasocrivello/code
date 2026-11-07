import mysql.connector


class DB_Connect:
    def __init__(self):
        pass

    def get_connection(self):
        # Manca il controllo degli errori
        cnx = mysql.connector.connect(option_files="./database/db.cnf")
        return cnx
