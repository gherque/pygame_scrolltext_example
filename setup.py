from setuptools import setup

setup(
    name="horizontalscroll",
    version="0.0.1",
    packages=["horizontalscroll"],
    entry_points={
        "console_scripts": [
            "horizontalscroll = horizontalscroll.__main__:main"
        ]
    },
)