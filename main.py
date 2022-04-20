from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import logging
from logging.config import dictConfig
from log_config import log_config

# dictConfig(log_config)
logger = logging.getLogger("reddit-broker-bot")

app = FastAPI()


# class PredictionRequest(BaseModel):
#     subreddit: str


@app.get("/")
def health():
    logger.info("Health request received.")
    return {"Status": "Service is online."}

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}