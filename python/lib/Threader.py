import os, sys
import threading

import logging
logger = logging.getLogger('RCScv')

class Threader(object):

    def __init__(self, name, limit=0, logger=None, buffer=[], active=0):
        self.name = name
        self.limit = limit
        self.logger = logger
        self.buffer = buffer
        self.active = active

        if self.logger is None:
            logger = logging.getLogger('RCScv')

    def run(self, fn, args):
        assert fn is not None, 'Thread must have a function to execute'
        assert callable(fn), 'fn parameter must be a function'

        logger.debug('Adding Thread %s' % self.name)

        args.logger = self.logger
        t = threading.Thread(target=fn, args=args)

    """
    def add(self, fn):
        assert fn is not None, 'Thread must have a function to execute'
        assert callable(fn), 'fn parameter must be a function'

        logger.info('Adding Thread %s' % self.name)

        t = threading.Thread(target=fn)
        self.buffer.append(t)
        self.active += 1

    def run_buffer(self):
        logger.info('Beginning thread listener %s' % self.name)

        while len(self.buffer) > 0:
            while active >= self.limit:
                pass #wait until barrier is reached
            
            t = self.buffer.pop(0)
            t.start()
            active = active - 1

            logger.debug('Began thread for %s. [Active: %s :: Limit: %s]' % 
                (self.name, active, self.limit))

    def run_async(self):
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
    """

