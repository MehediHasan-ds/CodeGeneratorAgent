# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import router

app = FastAPI(
    title="AI Code Generator API",
    description="AI-powered code generation using Groq/Llama",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api", tags=["generation"])

@app.get("/")
async def root():
    return {"message": "AI Code Generator API is running!", "docs": "/docs"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "CodeGenerator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)