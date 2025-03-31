from setuptools import setup, find_packages

setup(
    name="nnk_unzip",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["questionary"],
    entry_points={
        "console_scripts": [
            "nnk_unzip=nnk_unzip.__main__:main",
        ],
    },
)
