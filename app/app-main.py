import json
import logging
import os
from lib.timer import Timer
from flask import Flask, request
from urllib.request import urlopen

app = Flask(__name__)

log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO"))
app.logger.setLevel(log_level)

global_flag = {'enabled': False}

@app.route("/")
def hello_world():
    delay_sec = int(request.args.get("delay_sec"))

    odd = is_even(delay_sec)
    app.logger.debug(f'Turning the flag "{odd}"')
    global_flag['enabled'] = odd

    with (
        Timer(app.logger, f"delay_sec={delay_sec}"),
        urlopen(f"http://app-api?delay_sec={delay_sec}") as f
    ):
        # XXX: Demonstrating that this doesn't always return "True" for even numbers
        #      as multiple requests change the one global/shared variable.
        app.logger.debug(f'The flag is "{global_flag["enabled"]}" for delay_sec={delay_sec}')
        return json.load(f)


def is_even(num): return num % 2 == 0