from setuptools import setup

setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line Task-app weitten in Python',
    author='Deeb Hajjar',
    install_require=['tabulate'],
    entry_points={
        'console_scripts': [
            'taskaty=taskaty:main'
        ],
    },
)