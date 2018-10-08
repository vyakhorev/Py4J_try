
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

class PythonScriptCallback:
    '''
    1. Java application calls   public Double callPythonServerScriptFunction(String function_name).
    2. This call spawns PythonScriptCallback instance and calls
    3. Python calls
    '''

    class Java:
        implements = ["py4jJavaCalcServer.PythonScriptCallback"]

    def __init__(self, server, script):
        self.server = server
        self.script = script
        self.script_name = script.__name__  # function name to be precise

    def __repr__(self):
        return "a callback to {}".format(self.script_name)

    def get_script_name(self) -> str:
        return self.script_name

    def calculate(self, calc_context) -> float:
        print(calc_context.__class__)
        ans = self.script()
        logger.debug("{} is called".format(self.script_name))
        return ans
