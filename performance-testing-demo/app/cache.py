import time
from typing import Any, Dict

# simple in-memory cache simulation
cache: Dict[str, Any] = {}
cache_stats = {"hits": 0, "misses": 0}

# simulate a slow DB fetch
def slow_db_call(key: str):
    # realistic delay for a db call / remote API
    time.sleep(0.5)
    if key == "users":
        return ["Alice", "Bob", "Charlie"]
    return {"key": key, "value": "demo"}

def get_data_with_cache(key: str):
    if key in cache:
        cache_stats["hits"] += 1
        return {"data": cache[key], "source": "cache"}
    else:
        cache_stats["misses"] += 1
        data = slow_db_call(key)
        cache[key] = data
        return {"data": data, "source": "database"}

def get_cache_metrics():
    total = cache_stats["hits"] + cache_stats["misses"]
    hit_rate = (cache_stats["hits"] / total * 100) if total > 0 else 0.0
    return {"hits": cache_stats["hits"], "misses": cache_stats["misses"], "hit_rate": round(hit_rate, 2)}

# helper to reset metrics (useful between runs)
def reset_cache():
    cache.clear()
    cache_stats["hits"] = 0
    cache_stats["misses"] = 0
