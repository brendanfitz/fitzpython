import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'matplotlib',
]

setuptools.setup(
    name="fitzpython-fitzbuzz", # Replace with your own username
    version="0.0.1",
    author="Brendan Fitzpatrick",
    author_email="brendanjfitzpatrick0@gmail.com",
    description="Brendan Fitzpatrick's personal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fitzbuzz/fitzpython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.6',
)