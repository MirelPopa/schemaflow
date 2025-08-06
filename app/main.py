from fastapi import FastAPI

from app.api.v1 import api_router

app = FastAPI(title="SchemaFlow")
app.include_router(api_router)
