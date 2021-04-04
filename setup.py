from setuptools import setup

setup(
    name="verticalscroll",
    version="0.0.1",
    packages=["verticalscroll"],
    entry_points={
        "console_scripts": [
            "verticalscroll = verticalscroll.__main__:main"
        ]
    },
)