__author__ = 'Igor Barulin'


import unittest

from queue import Queue


class TestQueueEnqueueArg(unittest.TestCase):

	def setUp(self):
		self.queue = Queue(1)

	def testQueueEnqueueArgStr(self):
		with self.assertRaises(BaseException):
			self.queue.enqueue('1')

	def testQueueEnqueueArgFloat(self):
		with self.assertRaises(BaseException):
			self.queue.enqueue(1.0)