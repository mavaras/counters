import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='counters-mavaras',
    version='0.0.1',
    author='Example Author',
    author_email='maario.vrs@gmail.com',
    description='Function call counter and code flow display',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mavaras/counters',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)