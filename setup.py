from setuptools import setup, find_packages

setup(
    name='mylib',
    version='0.0.3',
    description='my functions',
    url='github-my_library',
    author='wesleyok',
    author_email='yoojaemyeong@gmail.com',
    license='free',
    packages=find_packages(),
    install_requires=['numpy'],
)
