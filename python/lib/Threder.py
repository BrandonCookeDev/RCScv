import os, sys
import threading

import logging
logger = logging.getLogger('RCScv')

class Worker(object):

    def __init__(self, name, limit=0, buffer=[], active=0):
        self.name = name
        self.limit = limit
        self.buffer = buffer
        self.active = active

    def add(fn):
        assert fn is not None, 'Thread must have a function to execute'
        assert callable(fn), 'fn parameter must be a function'

        logger.info('Adding Thread %s' % self.name)

        t = threading.Thread(target=fn)
        self.buffer.append(t)
        self.active += 1

    def run():
        logger.info('Beginning thread listener %s' % self.name)

        while len(self.buffer) > 0:
            while active >= self.limit:
                pass #wait until barrier is reached
            
            t = self.buffer.pop(0)
            t.start()
            active = active - 1

            logger.debug('Began thread for %s. [Active: %s :: Limit: %s]' % 
                (self.name, active, self.limit))

    def run_async():
        '''
        DON'T USE THIS YET
        '''
        logger.info('Beginning thread listener %s' % self.name)

        #continue processing 
        active = 0
        while True: 
            while len(self.buffer) > 0:
                while active >= self.limit:
                    pass #wait until barrier is reached
                
                t = self.buffer.pop(0)
                t.start()
                active = active - 1

                logger.debug('Began thread for %s. [Active: %s :: Limit: %s]' % 
                    (self.name, active, self.limit))


