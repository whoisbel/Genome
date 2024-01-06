from setuptools import setup, find_packages

setup(
    name='genome',
    version='1',
    packages=find_packages(),
    install_requires=[
        'regex',
        'bs4'
    ],
    entry_points={
        'console_scripts': [
            'genome=genome.genome:main',
        ],
    },
    author='Michael John Angelo Belciña',
    author_email='mjabelcina@gmail.com',
    description='Genome: A Python templating engine for dynamic and personalized interfaces with embedded Python code in HTML templates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/whoisbel/genome',
    license='Apache-2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License 2.0',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)