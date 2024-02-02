from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import todos

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(todos.router)

@app.get("/")
async def root():
  return {"data" : "fastapi-mongoDB"}