from fastapi import FastAPI 
from api import router 
# --------------------------------------------------- 
# FastAPI Application Initialization 
# --------------------------------------------------- 
app = FastAPI( title="AI UAV Surveillance System", description="Backend server for UAV monitoring and AI analytics.", version="1.0.0" ) 
# --------------------------------------------------- 
# Include API Routes 
# --------------------------------------------------- 
app.include_router(router) 
# --------------------------------------------------- 
# Root Endpoint 
# --------------------------------------------------- 
@app.get("/") 

def home(): 
    """ Root endpoint used to verify backend status. """ 
    return { "status": "Backend Running", "system": "AI UAV Surveillance System" }
