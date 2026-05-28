from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()

@app.get("/")
def home():
    """
    Default API route.
    Used to verify backend status.
    """

    return {
        "status": "Backend Running",
        "system": "AI UAV Surveillance System"
    }
