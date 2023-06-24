from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

import json

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return {"test": "done"}