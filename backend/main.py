from fastapi import FastAPI, Depends
from fastapi_throttle import RateLimiter

app = FastAPI()

# Limit to 5 requests per minute
limiter = RateLimiter(times=5, seconds=60)

@app.get("/", dependencies=[Depends(limiter)])
async def root():
    return {"message": "Hello World"}