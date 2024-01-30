from setuptools import setup, find_packages

setup(
    name='ByPassSafe',
    version='0.4',  # Atualize o número da versão conforme necessário
    packages=find_packages(),
    install_requires=[
        'psycopg2',
        'bcrypt',
    ],
    entry_points={
        'console_scripts': [
            'ByPassSafe = bypassafe.main:main',
        ],
    },
)
