class PythonListener:
    '''
    This class implements Java interface py4jGreendata.ExampleListener
    Use this for callbacks.
    '''

    class Java:
        implements = ["py4jJavaCalcServer.PythonListenerInterface"]

    def __init__(self, server):
        self.server = server

    def notify(self, obj):
        # # This would be called back from Java
        # print("Notified by Java")
        #         # print(obj)
        self.server.print_to_java_console('hello from python!')
        return "A Return Value"