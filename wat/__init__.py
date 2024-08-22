import sys

from .inspection.inspection import wat
from .version import __version__

__all__ = [
    'wat',
    '__version__',
]

sys.modules['wat'] = wat  # type: ignore
setattr(wat, '__version__', __version__)

// Root Layout and Protected Routes1

// Root Layout and Protected Routes1


// Root Layout and Protected Routes3
