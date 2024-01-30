from setuptools import setup, find_packages

setup(
    name='ByPassSafe',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'passlib',
    ],
    entry_points={
        'console_scripts': [
            'ByPassSafe = ByPassSafe.main:main',
        ],
    },
)
