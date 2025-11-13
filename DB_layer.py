import json
import pyodbc
import pandas as pd


credsfilepath="db_creds.json"


def initialize_connection():
    jsonfile = open(credsfilepath)
    credsObj=json.load(jsonfile)
    
    conn = pyodbc.connect(
                        'Driver={0};Server={1};Database={2};UID={3};PWD={4};Trusted_Connection=no;'
                        .format(credsObj["driver"],credsObj["server"],credsObj["DB"],credsObj["user"],credsObj["pass"]))
    
    cursor = conn.cursor()
    jsonfile.close()
    return conn,cursor

def close_connection(conn):
    conn.close()

def select_from_table(query):
    con,cur=initialize_connection()    
    df = pd.read_sql(query,con)
    #print(df)
    close_connection(con)
    return df

def insert_into_table(query):
    con,cur=initialize_connection()
    cur.execute(query)
    res = cur.fetchone()[0]
    con.commit()
    return res

def insert_into_table_no_generated_ID(query):
    con,cur=initialize_connection()
    cur.execute(query)
    
    con.commit()


#initialize_connection()
#insert_into_table("insert into LoginUsers values ('user2','password321','user')")
#dataframe = select_from_table("select * from [K2_eServices].[Common].[Request]")






