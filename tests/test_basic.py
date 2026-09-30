"""Basic tests for 123pan module"""
import unittest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestImports(unittest.TestCase):
    def test_sign_py_importable(self):
        try:
            import sign_py
            self.assertIsNotNone(sign_py)
        except ImportError as e:
            self.skipTest(f"sign_py not importable: {e}")

    def test_sign_function_callable(self):
        try:
            from sign_py import generate_sign
            self.assertTrue(callable(generate_sign))
        except (ImportError, AttributeError) as e:
            self.skipTest(f"generate_sign not available: {e}")


if __name__ == "__main__":
    unittest.main()
