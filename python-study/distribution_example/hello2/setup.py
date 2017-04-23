from setuptools import setup

setup(
    name="hello2",
    version="1",
    packages=["hello2"],
    entry_points={
        "pytimed": [
            "hello2 = hello2.hello2:say_hello",
        ]
    },)
