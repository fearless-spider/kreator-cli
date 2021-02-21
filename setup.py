
from setuptools import setup, find_packages
from kreator.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='kreator',
    version=VERSION,
    description='Create python project from command line',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='FEARLESS SPIDER',
    author_email='office@fearlessspider.com',
    url='https://fearlessspider.com',
    license='BSD 3-Clause "New" or "Revised" License',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'kreator': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        kreator = kreator.main:main
    """,
)
