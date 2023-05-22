from setuptools import setup

setup(
    name="fraggler",
    version="0.1.0",
    description="Fragment Analysis package in python!",
    url="https://github.com/willros/fraggler",
    author="William Rosenbaum and Pär Larsson",
    author_email="william.rosenbaum@umu.se",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "networkx",
        "lmfit",
        "scipy",
        "biopython",
        "panel",
        "fire",
    ],
    #packages=setuptools.find_packages(exclude=["dist", "build", "*.egg-info", "tests"]),
    entry_points={"console_scripts": ["fraggler=fraggler.cli:run"]},
)