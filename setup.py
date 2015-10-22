# from distutils.core import setup
from setuptools import setup

setup(
    name='markdown-magic',
    version='1.0',
    maintainer='Radhika Ghosal',
    maintainer_email='radhikaghosal@gmail.com',
    url='https://github.com/RadhikaG/markdown-magic',
    py_modules=['magic'],
    install_requires=['markdown>=2.5'],
    license='MIT',
    description='Create memes and find best-fitting gifs using Python-Markdown.',
    keywords=['markdown','markup','memes','gifs','plugin'],

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
        ],

    long_description=open('README.rst').read(),
)
