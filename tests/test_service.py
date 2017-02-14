import unittest
from app.service import app

class TestService(unittest.TestCase):

	def setUp(self):
		self.app_test_client = app.test_client()

	def testHello(self):
		r = self.app_test_client.get('/')
		self.assertEquals('Hello', r.data)

	def testHelloName(self):
		r = self.app_test_client.get('/Joe')
		self.assertEquals('Hello Joe', r.data)

	def testHelloNameAge(self):
		r = self.app_test_client.get('/Joe/40')
		self.assertEquals('Hello Joe you are now 40', r.data)
