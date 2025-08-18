from fastapi import FastAPI, Depends
from fastapi_throttle import RateLimiter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Deal with cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Limit to 5 request per second
limiter = RateLimiter(times=5, seconds=1)

@app.get("/", dependencies=[Depends(limiter)])
async def root():
    return {"message": "Hello World"}
