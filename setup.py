import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='exponea-python-sdk',
    version='0.2.0',
    author='Exponea',
    author_email='info@exponea.com',
    description='A Python client for Exponea Data API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/exponea/exponea-python-sdk',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    )
)
