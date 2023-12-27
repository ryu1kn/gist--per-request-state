from time import time


class Timer:
    def __init__(self, logger, message):
        self._logger = logger
        self._message = message

    def __enter__(self):
        self._logger.info(f"[BEGIN] processing {self._message}")
        self._begin_at = time()

    def __exit__(self, *args):
        elapsed_sec = time() - self._begin_at
        self._logger.info(f"[END] processing {self._message}, elapsed {elapsed_sec:.2f} sec")
