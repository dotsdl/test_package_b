"""
Unit and regression test for the test_package_b package.
"""

# Import package, test suite, and other packages as needed
import sys

def test_test_package_b_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "test_package_b" in sys.modules
