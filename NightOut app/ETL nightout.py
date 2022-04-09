import psycopg2
import pandas as pd

db = psycopg2.connect(
    user='aulaspl',
    password='aulaspl',
    host='127.0.0.1',
    port='5432',
    database='NightShiftApp'
)