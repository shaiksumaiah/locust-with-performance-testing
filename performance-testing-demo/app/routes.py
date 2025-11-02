from fastapi import APIRouter
import time
from .cache import get_data_with_cache, get_cache_metrics, reset_cache

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    # simulate a moderately slow endpoint (like a DB query + processing)
    time.sleep(0.2)
    return {"tasks": ["task1", "task2", "task3"]}

@router.get("/users")
def get_users():
    # uses our in-memory cache simulation
    return get_data_with_cache("users")

@router.get("/cache-metrics")
def cache_metrics():
    # return cache stats
    return get_cache_metrics()

@router.post("/cache-reset")
def cache_reset():
    reset_cache()
    return {"message": "cache reset"}
