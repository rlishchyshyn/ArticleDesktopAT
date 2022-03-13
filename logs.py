import logging
import os
import time

import coloredlogs

if not os.path.exists("logs"):
    os.makedirs("logs")

fmt = '%(asctime)s,%(msecs)03d %(levelname)s %(message)s'
logging.basicConfig(filename=f'logs/log_{int(time.time()*1000)}.log', filemode='w', format=fmt)
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt=fmt,
                    level_styles={'critical': {'bold': True, 'color': 'red'},
                                  'debug': {'color': 'green'},
                                  'error': {'color': 'red'},
                                  'info': {'color': 'blue'},
                                  'notice': {'color': 'magenta'},
                                  'spam': {'color': 'green', 'faint': True},
                                  'success': {'bold': True, 'color': 'green'},
                                  'verbose': {'color': 'blue'},
                                  'warning': {'color': 'yellow'}},
                    field_styles={'asctime': {'color': 'green', 'faint': True},
                                  'levelname': {'bold': True, 'color': 'yellow'},
                                  'name': {'color': 'blue'},
                                  'programname': {'color': 'cyan'}},
                    )
