import setuptools
from setuptools import setup

setup(
    name='ioflow',
    version='0.4.3',
    packages=setuptools.find_packages(),
    setup_requires=[
        'tensorflow',
        'tokenizer_tools'
    ],
    url='',
    license='',
    author='Xiaoquan Kong',
    author_email='u1mail2me@gmail.com',
    description='',
    install_requires=['numpy', 'requests', 'flask']
)
