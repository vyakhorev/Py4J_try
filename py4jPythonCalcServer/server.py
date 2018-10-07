
# Alternative (https://www.py4j.org/py4j_client_server.html#module-py4j.clientserver):
# from py4j.clientserver import ClientServer, JavaParameters, PythonParameters
# gateway = ClientServer(java_parameters=JavaParameters(), python_parameters=PythonParameters())

from py4j.java_gateway import JavaGateway, CallbackServerParameters

class RiskCalcServer:
    '''
    This server shall work
    '''

    def __init__(self):
        self.java_gateway = None  # gateway

    def start(self):
        # self.java_gateway.entry_point - a PythonServiceApp instance replica
        # self.java_gateway.jvm - jvm replica
        self.java_gateway = JavaGateway(callback_server_parameters=CallbackServerParameters())

    def shutdown(self):
        self.java_gateway.shutdown()

    def test_map(self):
        m = self.get_new_hashmap()
        m[1] = 'hello 1'
        m[2] = 'hello 1'
        m[3] = 'hello 3'
        self.java_gateway.entry_point.updateObjectData(m)

    def get_new_hashmap(self):
        # TODO: need some kind of HashMap typing + from dict transformation on python side
        return self.java_gateway.jvm.java.util.HashMap()

    def print_to_java_console(self, msg):
        self.java_gateway.jvm.System.out.println(msg)

    def register_listener(self, py_listener):
        self.java_gateway.entry_point.registerListener(py_listener)

    def notify_listeners(self):
        self.java_gateway.entry_point.notifyAllListeners()