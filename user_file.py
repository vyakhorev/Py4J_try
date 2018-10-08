
'''
By design, this file is edited by user.
Todo: multiple files design, call queue, non-static context
'''

import time  # TODO: Keras
import random

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

def HeavyCall():
    logger.debug("I am a really smart neuralnet that needs some time to think")
    time.sleep(1)
    logger.debug("Getting really convolutional")
    time.sleep(2)
    ans = random.random()
    logger.debug("I found it! The PD is equal to {}".format(ans))
    return ans


def SomeLogisticRegression():
    logger.debug("I wonder can I classify this mess?...")
    time.sleep(1)
    ans = random.choice([3.1415926, 2.718281828, 1.618033988])/10
    logger.debug("I'm certain that PD is equal to {}".format(ans))