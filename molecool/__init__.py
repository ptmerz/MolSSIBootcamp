"""
molecool
MolSSI bootcamp
"""

# Add imports here
from .functions import *
from .atom_data import atomic_weights, atom_colors

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
