import unittest
from unittest.suite import TestSuite
from home import test_home_up, dummy

if __name__ == "__main__":

	# create the suite from the test classes
    suite = TestSuite()
    # load the tests
    tests = unittest.TestLoader()

	# add the tests to the suite
    suite.addTests(tests.loadTestsFromModule(test_home_up))
    suite.addTests(tests.loadTestsFromModule(dummy))
    # suite.addTests(tests.loadTestsFromTestCase(TestHomepageUp))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)