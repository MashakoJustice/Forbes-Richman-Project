from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude = ['tests*']),
    license='MIT',
    description='Rich List Analysis',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MashakoJustice/Forbes-Richman-Project.git',
    author='Mashako Justice Manyelo, Mpho Seseti, Jonathan Thomson',
    author_email='manyelojustice@gmail.com, jonathanthomson2004@gmail.com, mphoses@hotmail.com'
)