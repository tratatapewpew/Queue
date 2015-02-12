__author__ = 'Igor Barulin'


import unittest

from queue import Queue


class TestQueueFull(unittest.TestCase):

	def setUp(self):
		self.queue = Queue(3)
		for i in range(3):
			self.queue.enqueue(i)

	def testQueueFullIsNotEmpty(self):
		self.assertEqual(self.queue.empty(), False)

	def testQueueFullIsFull(self):
		self.assertEqual(self.queue.full(), True)

	def testQueueEnqueue(self):
		self.assertEqual(self.queue.enqueue(3), False)

	def testQueueDequeue(self):
		self.assertEqual(self.queue.dequeue(), 0)
		self.assertEqual(self.queue.full(), False)