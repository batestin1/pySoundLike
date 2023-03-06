
from setuptools import setup

setup(
    name = 'pySoundLike',
    version = '1.0.0',
    author = 'bates',
    author_email = 'bates@mailer.com.br',
    packages = ['pySoundLike'],
    description = 'a way to make your life easier',
    long_description = 'file: README.md',
    url = 'https://github.com/batestin1/',
    project_urls = {'Codigo fonte': 'https://github.com/batestin1/', 'Download': 'https://github.com/batestin1/'},
    keywords = 'a way to make your life easier',
    classifiers = [],
    install_requires=[
        'pronouncing',
        'random'
    ]
)