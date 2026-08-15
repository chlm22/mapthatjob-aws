from fastapi import FastAPI
from mangum import Mangum
app = FastAPI()

#ENDPOINT SECTIONNNNN
#homepage
@app.get("/")
def read_root():
    return {"message": "Welcome to the MapThatJob API!"}

#jobs data
@app.get("/jobs")
def get_jobs():@app.get("/jobs")
def get_jobs():
    return {
        "jobs": [
            {"title": "Software Verification Engineer", "location": "Novi, MI"},
            {"title": "Backend Developer", "location": "Ann Arbor, MI"}
        ]
    }

#MANGUM FOR LAMBDA AWS
handler = Mangum(app)
