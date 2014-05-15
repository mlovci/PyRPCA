from setuptools import setup
from setuptools import find_packages

setup(
    name='pyrpca',
    packages=find_packages(),
    url='',
    license='',
    author='',
    author_email='',
    description='',
    include_package_data=True,
   
    install_requires=['setuptools',
                      'numpy >= 1.8.1 ',
                      'scipy >= 0.13.0',
                      'matplotlib >= 1.3.1',
    ],
    version = "0.0.1"
)
