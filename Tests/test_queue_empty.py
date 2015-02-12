__author__ = 'Igor Barulin'


import unittest

from queue import Queue


class TestQueueEmpty(unittest.TestCase):

	def setUp(self):
		self.queue = Queue(1)

	def testQueueEmptyIsEmpty(self):
		self.assertEqual(self.queue.empty(), True)

	def testQueueEmptyIsNotFull(self):
		self.assertEqual(self.queue.full(), False)

	def testQueueEmptyEnqueue(self):
		self.assertEqual(self.queue.enqueue(1), True)
		self.assertEqual(self.queue.empty(), False)

	def testQueueEmptyDequeue(self):
		self.assertEqual(self.queue.dequeue(), None)
