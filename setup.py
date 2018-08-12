import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exponea_python_sdk",
    version="0.1.0",
    author="Lukas Cerny",
    author_email="lukas.cerny@exponea.com",
    description="A Python client for Exponea Data API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukasotocerny/exponea-python-client",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)