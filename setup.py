from setuptools import setup, find_packages

setup(
    name="api-speed-test-websocket-20260603_231230",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'api=api:main',
        ],
    },
)
