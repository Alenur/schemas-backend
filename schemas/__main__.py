import logging

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from schemas.endpoints import routers
from schemas.utils.exceptions import BaseAPIException

logger = logging.getLogger(__name__)

app = FastAPI(title="Schemas")

app.include_router(routers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(BaseAPIException)
async def unicorn_exception_handler(request: Request, exc: BaseAPIException):
    logger.error(str(exc))
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.__repr__()},
    )


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
