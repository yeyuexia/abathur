# coding: utf8

from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="abathur",
    version="1.0.0",
    description="Template manager",
    long_description=long_description,
    url="https://github.com/yeyuexia/abathur",
    author="yeyuexia",
    author_email="yyxworld@gmail.com",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],
    keywords='manage project templates and build project with template',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'abathur=abathur.entrypoint:main',
        ],
    },
    install_requires=['mono-require', 'gitdb2', 'GitPython', 'smmap2'],
)
