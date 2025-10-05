import mysql.connector
from config import DB_CONFIG

def get_db_connection():
 try:
  con = mysql.connector.connect(**DB_CONFIG)
  return con
 except mysql.connector.Error as e:
  print("Database Connection Error:",e)
  return None