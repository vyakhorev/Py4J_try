
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

def NeuralNetCall(data_dict):
    logger.info("I am a really smart neuralnet and I need some time to think about this point of data")
    time.sleep(0.5)
    logger.info("So this is {}".format(data_dict))
    time.sleep(0.5)
    logger.info("Getting really convolutional")
    time.sleep(2)
    ans = random.random()
    logger.info("I found it! The PD is equal to {}".format(ans))
    return ans


def SomeLogisticRegression(data_dict):
    logger.info("I wonder can I classify this mess?... This is some peace of outliner {}".format(data_dict))
    time.sleep(1)
    ans = random.choice([3.1415926, 2.718281828, 1.618033988])
    logger.info("have no idea what PD is but the answer should be equal to {}".format(ans))
    return ans