# 🗺️ MapThatJob 

MapThatJob is a full-stack serverless web application that visualizes job postings on an interactive map. It fetches real-time job data, geocodes the locations, and plots them to help users geographically organize their job search. It is basically like a Zillow for jobs!


## 🏗️ Architecture

This project was intentionally designed using a highly scalable, zero-cost serverless architecture on AWS.

*   Frontend: React.js hosted securely on an Amazon S3 Bucket and distributed globally via Amazon CloudFront.
*   Backend: Python and FastAPI, wrapped with Mangum, and deployed serverlessly via AWS Lambda and API Gateway.
*   Database: Serverless PostgreSQL (Neon) accessed via raw SQL using psycopg2.
*   CI/CD Pipeline: Fully automated testing and deployment using GitHub Actions.


## 🚀 Features
*   Geospatial Visualization: Converts city/state location data from job APIs into exact latitude and longitude coordinates.
*   Serverless Scalability: Backend infrastructure scales to zero when not in use and automatically spins up to handle concurrent requests.
*   Automated Data Pipeline: A scheduled Python job fetches, cleans, and inserts new job postings directly into the PostgreSQL database using parameterized raw SQL queries.


## 🛠️ Local Development Setup

### Prerequisites
* Python 3.10+
* Node.js & npm
* A free Neon PostgreSQL database URL

### Backend Setup (FastAPI)
1. Clone the repository: git clone https://github.com/yourusername/MapThatJob.git
2. Navigate to the backend: cd backend
3. Create a virtual environment: python -m venv venv
4. Activate the environment: 
   * Windows: venv\Scripts\activate
   * Mac/Linux: source venv/bin/activate
5. Install dependencies: pip install -r requirements.txt
6. Create a .env file and add your database URL: DATABASE_URL=your_neon_url_here
7. Start the local server: uvicorn main:app --reload
   * *The interactive API documentation will be available at `http://localhost:8000/docs`*

### Frontend Setup (React)
1. Navigate to the frontend directory: cd frontend
2. Install dependencies: npm install
3. Start the development server: npm start


## 🧪 Testing & CI/CD

This project utilizes GitHub Actions for Continuous Integration and Continuous Deployment. 
Every push to the main branch triggers an automated workflow that:
1. Provisions an Ubuntu runner.
2. Installs all Python dependencies.
3. Executes isolated unit and integration tests using pytest to verify the API endpoints and database adapters.
4. Upon passing all tests, packages the backend environment and deploys it directly to AWS Lambda.

