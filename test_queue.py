__author__ = 'Igor Barulin'


import unittest

testmodules = [
    'QueueTests.test_queue_constructor',
    'QueueTests.test_queue_enqueue_arg',
    'QueueTests.test_queue_empty',
    'QueueTests.test_queue_partial',
    'QueueTests.test_queue_full',
    'QueueTests.test_queue_fifo'
    ]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)