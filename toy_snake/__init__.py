from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("toy_snake")
except PackageNotFoundError:
    # package is not installed
    pass
