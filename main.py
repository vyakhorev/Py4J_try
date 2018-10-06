
from pygreendata.listener import PythonListener
from pygreendata.server import GreendataCalcServer

__author__ = "Alexey Vyakhorev"


if __name__ == "__main__":
    py_server = GreendataCalcServer()  # uses Py4J event loop
    py_server.start()

    listener = PythonListener(py_server)
    listener2 = PythonListener(py_server)
    py_server.register_listener(listener)
    py_server.register_listener(listener2)
    py_server.notify_listeners()

    py_server.shutdown()