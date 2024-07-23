from setuptools import find_packages, setup

setup(
    name='sysRecurseSearch',
    packages=find_packages(include=['sysRecurseSearch']),
    version='0.1.0',
    description='My first Python library',
    author='Corrina Alcoser aka Core-Creates',
    install_requires=[],
    setup_requires=['os', 'time', 'stat'],
)