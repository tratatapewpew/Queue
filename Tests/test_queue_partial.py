__author__ = 'Igor Barulin'


import unittest

from queue import Queue


class TestQueuePartial(unittest.TestCase):

	def setUp(self):
		self.queue = Queue(3)
		for i in range(2):
			self.queue.enqueue(i)

	def testQueueParitalIsNotEmpty(self):
		self.assertEqual(self.queue.empty(), False)

	def testQueuePartialIsNotFull(self):
		self.assertEqual(self.queue.full(), False)