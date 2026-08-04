from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.api.v1.router import router
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI application FIRST
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Personalized Notification Intelligence",
    version=settings.APP_VERSION,
)

# Configure middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(router)


@app.get("/")
async def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "model": settings.LLM_MODEL,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "backend",
    }
print("\n========== REGISTERED ROUTES ==========")
for route in app.routes:
    print(route.path)
print("=======================================\n")