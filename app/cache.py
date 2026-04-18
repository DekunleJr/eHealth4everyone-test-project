import redis
import json
import requests
from app.config import REDIS_URL

r = redis.from_url(REDIS_URL)

def get_external_data():
    cache_key = "external_api_data"

    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1").json()

    r.setex(cache_key, 3600, json.dumps(response))  # 1 hour TTL

    return response