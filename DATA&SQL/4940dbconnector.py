import pyodbc as sql
import pandas as pd
import os


conn = sql.connect('Driver={SQL Server};'
                      'Server=REDFIRE\SQLEXPRESS;'
                      'Database=MMUCC_SeniorProgram;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

def writecsv(filename,query=None):
    query.to_csv('csvs/'+filename+".csv",index=False)

if __name__ == '__main__':
    if not os.path.exists('csvs'):
        os.makedirs('csvs')

    with open('queries.txt','r') as procedures:
        for line in procedures:
            print("exec " + line.strip())
            sql_query = pd.read_sql_query("exec " + line.strip(), conn)
            writecsv(line.strip(), sql_query)

    cursor.close()
    conn.close()