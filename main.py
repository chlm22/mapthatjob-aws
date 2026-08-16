from fastapi import FastAPI, HTTPException
from mangum import Mangum
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

DB_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    try:
        conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

@app.get("/")
def read_root():
    return {"message": "Welcome to the MapThatJob API!"}

@app.get("/jobs")
def get_jobs():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Could not connect to the database")
    
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, location, latitude, longitude FROM jobs;")
    jobs_data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return {"jobs": jobs_data}

handler = Mangum(app)
