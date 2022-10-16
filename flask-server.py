#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
from core.application import app
from helpers.loggers import get_logger

logger = get_logger(__file__)


if __name__ == '__main__':
    try:
        logging.info('Starting app... Press CTRL+C to quit.')
        app.run(host="0.0.0.0", port=9000, processes=2, threaded=False, debug=True)
    except KeyboardInterrupt:
        logging.info('Quitting... (CTRL+C pressed)')
        sys.exit(0)
    except Exception:  # Catch-all for unexpected exceptions, with stack trace
        logging.exception(f'Unhandled exception occurred!')
        sys.exit(1)
