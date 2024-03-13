from setuptools import setup

setup(
    name='jupiterpy',
    version='0.1.0',    
    description='A package to check Jupiter prices',
    url='https://github.com/bomsauro/jupiterpy',
    author='Bomsauro',
    author_email='bomsauro@gmail.com',
    license='BSD 2-clause',
    packages=['jupiterpy'],
    install_requires=['requests']
)