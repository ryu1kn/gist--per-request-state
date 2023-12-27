from asyncio import sleep
from json import dumps
import logging
import os
from lib.timer import Timer
from flask import Flask, request

app = Flask(__name__)

log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO"))
app.logger.setLevel(log_level)

@app.route("/")
async def hello_world():
    delay_sec = int(request.args.get("delay_sec"))

    with Timer(app.logger, f"delay_sec={delay_sec}"):
        await sleep(delay_sec)
        return dumps({"delayed": delay_sec})
