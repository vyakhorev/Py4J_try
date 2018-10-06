
from py4jPythonCalcServer.listener import PythonListener
from py4jPythonCalcServer.server import RiskCalcServer

__author__ = "Alexey Vyakhorev"


if __name__ == "__main__":
    py_server = RiskCalcServer()  # uses Py4J event loop
    py_server.start()

    listener = PythonListener(py_server)
    listener2 = PythonListener(py_server)
    py_server.register_listener(listener)
    py_server.register_listener(listener2)
    py_server.notify_listeners()

    py_server.shutdown()