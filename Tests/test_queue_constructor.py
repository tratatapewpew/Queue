__author__ = 'Igor Barulin'


import unittest

from queue import Queue


class TestQueueConstructor(unittest.TestCase):

	def testQueueConstructorZero(self):
		with self.assertRaises(BaseException):
			queue = Queue(0)

	def testQueueConstructorStr(self):
		with self.assertRaises(BaseException):
			queue = Queue("1")

	def testQueueConstructorFloat(self):
		with self.assertRaises(BaseException):
			queue = Queue(1.0)