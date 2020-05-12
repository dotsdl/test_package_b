"""
test_package_b
The second of two packages to test implicit namespaces.
"""

# Add imports here
from .test_package_b import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
