import app
import unittest

class TestApp(unittest.TestCase):

  def setUp(self):
    app.app.testing = True
    self.app = app.app.test_client()

if __name__ == '__main__':
  unittest.main()
