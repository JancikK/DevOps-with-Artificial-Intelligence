from setuptools import setup

setup(
    name="hello_package",
    version="0.1",
    py_modules=["hello"],
    entry_points={
        "console_scripts": [
            "hello=hello:say_hello"
        ]
    },
)
