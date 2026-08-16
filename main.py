from fastapi import FastAPI,HTTPException
from mangum import Mangum
import os
import psycopg2
from psycog2.extras import RealDictCursor

app = FastAPI()
DB_URL: os.environ.get("DATABASE_URL")

def get_db_connection():
    try:
        # RealDictCursor automatically formats your SQL rows into perfect JSON dictionaries!
        conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

#ENDPOINT SECTIONNNNN
#homepage
@app.get("/")
def read_root():
    return {"message": "Welcome to the MapThatJob API!"}


#jobs data
@app.get("/jobs")
def get_jobs():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Could not connect to the database")
    
    cursor = conn.cursor()
    
    # SQL query 
    cursor.execute("SELECT id, title, company, location, latitude, longitude FROM jobs;")
    jobs_data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return {"jobs": jobs_data}


#MANGUM FOR LAMBDA AWS
handler = Mangum(app)
