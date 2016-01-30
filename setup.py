from setuptools import setup

setup (name='ds_algorithms',
    version='0.1',
    description='Common Data Structures and Algorithms in Python',
    url='',
    author='Anthony Najjar Simon',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=['lib'],
    zip_safe=False)