__author__ = 'Igor Barulin'


import unittest

from queue import Queue


class TestQueueFIFO(unittest.TestCase):

	def setUp(self):
		self.queue = Queue(10)
		for i in range(10):
			self.queue.enqueue(i)

	def testQueueFIFO(self):
		for i in range(10):
			self.assertEqual(self.queue.dequeue(), i)