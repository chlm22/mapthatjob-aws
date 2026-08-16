from fastapi import FastAPI
from mangum import Mangum
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

DB_URL = os.environ.get("DATABASE_URL")

@app.get("/")
def read_root():
    return {"message": "Welcome to the MapThatJob API!"}

@app.get("/jobs")
def get_jobs():
    try:
        # connection inside the route to catch the error
        conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, company, location, latitude, longitude FROM jobs;")
        jobs_data = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"jobs": jobs_data}
        
    except Exception as e:
        return {
            "CRASH_REPORT": str(e), 
            "URL_CHECK": str(DB_URL)
        }

handler = Mangum(app)
