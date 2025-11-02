from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Performance Testing Demo")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Performance Testing API is running!"}
