import pyodbc
from sqlalchemy import create_engine
import pandas as pd
pyodbc.drivers()
import psycopg2

user='postgres'
password= 1234
host='localhost'
port='5432'
database='SPRINT_2'
db_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(db_url)
try:
    conn = engine.connect()
    print('Connection successful')
except Exception as e:
    print('Connection failed')
    print(e)
    
query = 'SELECT * FROM test_data.temptabla'
df = pd.read_sql(query, engine)
df