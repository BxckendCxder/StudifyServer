import mysql.connector

def ConectarDB():
    connection = mysql.connector.connect(
        host='192.168.0.12',
        user='D3CL0AK',
        password='STUDYFYADMON',
        database='studyfy'
    )
    return connection


