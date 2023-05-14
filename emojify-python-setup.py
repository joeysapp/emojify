# (todo) Install emojify-python as a package for use in CLI with setup_tools

from setuptools import setup, find_packages

# $ python3.8 emoji-python-setup.py developer
# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

# /opt/homebrew/lib/python3.8/site-packages/emojify-python.egg-link (link to .)
# /opt/homebrew/Cellar/python@3.8/3.8.13_3/Frameworks/Python.framework/Versions/3.8/bin

setup(
    name="emojify-python",
    version="0.0.0",    
    py_modules=["emojify-python"],
    python_requires="<=3.8.13",
    entry_points={
        "console_scripts": [
            # note: lol
        ],
    },
)
