import setuptools
import linecache2

setuptools.setup(
    version=linecache2.__version__,
    setup_requires=['pbr'],
    pbr=True)


