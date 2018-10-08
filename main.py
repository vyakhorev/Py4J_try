
'''
By design this application is supplied with open source
'''

__author__ = "Alexey Vyakhorev"

from py4jPythonCalcServer.interfaces.PythonScriptCallback import PythonScriptCallback
from py4jPythonCalcServer.server import RiskCalcServer

import time
import user_file

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

if __name__ == "__main__":
    # Start python server
    java_connector = RiskCalcServer()  # uses Py4J event loop
    java_connector.start()

    # register all callables from user_file (not the best design yet)
    for f in user_file.__dict__.values():
        if callable(f):
            callback = PythonScriptCallback(java_connector, f)
            java_connector.register_callback(callback)

    # shutdown after a ~minute
    for x in range(0, 59):
        time.sleep(1)
        if x%2 == 0: logger.debug('{} - tick'.format(x))
        else: logger.debug('{} - tock'.format(x))

    java_connector.shutdown()