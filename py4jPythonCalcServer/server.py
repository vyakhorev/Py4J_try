
# Alternative (https://www.py4j.org/py4j_client_server.html#module-py4j.clientserver):
# from py4j.clientserver import ClientServer, JavaParameters, PythonParameters
# gateway = ClientServer(java_parameters=JavaParameters(), python_parameters=PythonParameters())

from py4j.java_gateway import JavaGateway, CallbackServerParameters

class RiskCalcServer:
    '''
    This server shall work
    '''

    def __init__(self):
        self.java_gateway = None

    def start(self):
        self.java_gateway = JavaGateway(callback_server_parameters=CallbackServerParameters())

    def shutdown(self):
        self.java_gateway.shutdown()

    def print_to_java_console(self, msg):
        self.java_gateway.jvm.System.out.println(msg)

    def register_listener(self, py_listener):
        self.java_gateway.entry_point.registerListener(py_listener)

    def notify_listeners(self):
        self.java_gateway.entry_point.notifyAllListeners()