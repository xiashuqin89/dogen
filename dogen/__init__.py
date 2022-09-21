from dogen.version import version
from dogen.generator import Generator

__version__ = version

# Script that is executed in a script package if it exists and if
# no "exec" is explicitly defined
DEFAULT_SCRIPT_EXEC = "run"
# User used for executing scripts if no "user" is explicitly defined
DEFAULT_SCRIPT_USER = "root"
