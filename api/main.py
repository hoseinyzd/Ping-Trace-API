from fastapi import FastAPI
from api.services.ping_service import ping_host
from api.services.trace_service import trace_host

app = FastAPI(title="PingTrace API", version="1.0")

@app.get("/ping/{target}")
async def ping(target: str):
    result = ping_host(target)
    return {"reachable": result}

@app.get("/trace/{target}")
async def trace(target: str):
    return {"trace": trace_host(target)}
