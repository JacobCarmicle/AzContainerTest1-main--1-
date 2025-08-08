from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS to allow frontend calls (update origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev; restrict to your FE URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def get_message():
    return {"message": "Hello from Backend!"}