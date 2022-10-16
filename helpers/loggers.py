import logging
import os.path
import platform
from pathlib import Path
from logging.config import dictConfig

from wrappers.config_wrapper import ConfigWrapper


os_system = platform.system()


def disable_debug_mode_blocklist():
    logger_blocklist = [
        "telethon.client.telegrambaseclient",
        "telethon.extensions.messagepacker",
        "telethon.network.mtprotosender",
        "telethon.client.updates",
        "hpack.hpack",
        "httpx._client",
        "asyncio",
    ]

    for module in logger_blocklist:
        logging.getLogger(module).setLevel(logging.CRITICAL)


def get_logger(logger_name):
    logs_directory = os.path.join('..', 'logs')
    if not os.path.isdir(logs_directory):
        os.makedirs(logs_directory)

    logging_config = ConfigWrapper().get_config_file("logging")

    [keys.update({'filename': fr'{logs_directory}/{Path(logger_name).stem}-{handler.split("_")[0]}.log'})
     for handler, keys in logging_config['handlers'].items() if handler.endswith('handler')]

    disable_debug_mode_blocklist()

    dictConfig(logging_config)
    return logging.getLogger(logger_name)
