from fastapi import FastAPI
from routers import users, health_metrics, goals

app = FastAPI()

app.include_router(users.router)
app.include_router(health_metrics.router)
app.include_router(goals.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Personal Health Management API"}
