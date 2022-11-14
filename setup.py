from setuptools import setup

setup(
    name='phpipamsdk',
    version='0.0.1',
    description='FlipPipe PHPIPAM REST API Client',
    url='https://github.com/flippipe/python-phpipamsdk',
    author='FlipPipe',
    packages=['phpipamsdk', 'phpipamsdk.controllers'],
    zip_safe=False,
    install_requires=['requests']
)
