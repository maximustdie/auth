import uvicorn
from fastapi import FastAPI

from api import root_router

app = FastAPI()

app.include_router(root_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
