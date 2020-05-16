import pathlib
import sys

project_root = pathlib.Path(__file__).absolute().parent.parent
sys.path.insert(0, str(project_root))
