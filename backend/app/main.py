from fastapi import FastAPI

app = FastAPI(
    title="NexusNotify API",
    description="AI-Powered Notification Routing System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "status": "running",
        "project": "NexusNotify",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }