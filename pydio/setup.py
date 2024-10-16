from setuptools import setup, find_packages

setup(
    name='melodycoach',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'librosa',
        'pydub',
        'numpy',
        'matplotlib'
    ],
    description='A package for audio analysis and music feedback.',
    author='Yuriy Mysak',
    author_email='mysakyuriy@gmail.com',
    url='https://github.com/chairborn/pydio',
)