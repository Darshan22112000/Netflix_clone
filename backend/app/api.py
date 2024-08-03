import asyncio
import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore

from app.app_scheduler import Scheduler
from app.tmdb import Tmdb
from database.IO_ops import IO_ops

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

app = FastAPI()

# Initialize a SQLAlchemyJobStore with SQLite database
jobstores = {
    'default': MemoryJobStore()
}

# Initialize an AsyncIOScheduler with the jobstore
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='Asia/Kolkata')

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:4200",
    "localhost:4200"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# This is a scheduled job that will run every 10 seconds.
@scheduler.scheduled_job('interval', seconds=2400) #1 HOUR INTERVAL
def scheduled_job_1():
    asyncio.run(Scheduler.tmdb_refresh())
    print(f'Scheduler ran at:{datetime.datetime.now()}')

@app.on_event("startup")
async def startup_event():
    scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()

@app.get("/get_movies")
async def get_movies():
    resp = await IO_ops.get_movies()
    return {'results': resp.to_dict(orient='records')}

@app.get("/get_tv_shows")
async def get_tv_shows():
    resp = await IO_ops.get_tv_shows()
    return {'results': resp.to_dict(orient='records')}

@app.get("/get_rated_movies")
async def get_rated_movies():
    resp = await IO_ops.get_top_rated_movies()
    return {'results': resp.to_dict(orient='records')}

@app.get("/get_now_playing_movies")
async def get_now_playing_movies():
    resp = await IO_ops.get_now_playing_movies()
    return {'results': resp.to_dict(orient='records')}

@app.get("/get_popular_movies")
async def get_popular_movies():
    resp = await IO_ops.get_popular_movies()
    return {'results': resp.to_dict(orient='records')}

@app.get("/get_top_rated_movies")
async def get_top_ratedd_movies():
    resp = await IO_ops.get_top_rated_movies()
    return {'results': resp.to_dict(orient='records')}

@app.get("/get_upcoming_movies")
async def get_upcoming_movies():
    resp = await IO_ops.get_upcoming_movies()
    return {'results': resp.to_dict(orient='records')}



