
# Alternative (https://www.py4j.org/py4j_client_server.html#module-py4j.clientserver):
# from py4j.clientserver import ClientServer, JavaParameters, PythonParameters
# gateway = ClientServer(java_parameters=JavaParameters(), python_parameters=PythonParameters())

from py4j.java_gateway import JavaGateway, CallbackServerParameters

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

class RiskCalcServer:

    def __init__(self):
        self.java_gateway = None  # gateway

    def start(self):
        # self.java_gateway.entry_point - a PythonServiceApp instance replica
        # self.java_gateway.jvm - jvm replica
        self.java_gateway = JavaGateway(callback_server_parameters=CallbackServerParameters())
        self.java_gateway.setPythonCalcServerStatusAlive()
        logger.info("String the server")

    def shutdown(self):
        self.java_gateway.setPythonCalcServerStatusDead()
        self.java_gateway.shutdown()
        logger.info("Shutting down the server")

    def register_callback(self, new_callback):
        self.java_gateway.registerCallback(new_callback)
        logger.info("Registering the callback")
