
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


# TODO: heap queue in calculate call to manage the load
class PythonScriptCallback:
    '''
    1. On statup we create an instance of this class per function in user_file.py.
    2. RiskCalcServer.register_callback(callback) registers this instance in Java application.
    3. When needed, Java application calls public Double callPythonScript(String script_name)
       and passes immutable data (a dictionary with strings-numbers) into it. This invokes
       calculate(self, calc_context) call.
    '''

    class Java:
        implements = ["py4jJavaCalcServer.PythonScriptCallback"]

    def __init__(self, server, script):
        '''
        :param server: RiskCalcServer instance. Not in use yet.
        :param script: python callable that can take a dictionary.
        '''
        self.server = server
        self.script = script
        self.script_name = script.__name__  # function name to be precise

    def __repr__(self):
        return "a callback to {}".format(self.script_name)

    def get_script_name(self) -> str:
        '''
        :return: a unique-per-app string. Shall be used as a key to call this script
        '''
        return self.script_name

    def calculate(self, calc_context) -> float:
        '''
        :param calc_context: py4j.java_collections.JavaMap instance - works as a regular dict()
        :return: some float number that results from this calculation
        '''
        ans = self.script(calc_context)
        logger.info("{} is called".format(self.script_name))
        return ans
