from setuptools import setup, find_packages

setup(
    name="lcft",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pynacl==1.4.0",
        "cryptography==41.0.3"
    ],
    entry_points={
        "console_scripts": [
            "lcft=lcft.main:main"
        ]
    },
)