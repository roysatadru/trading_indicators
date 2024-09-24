from setuptools import setup, find_packages

# ignore packages list from requirements.txt
ignore_packages = ['setuptools']

setup(
  name='trading_indicators',
  # read from the version.txt file
  version=open('version.txt').read().strip(),
  packages=find_packages(),
  install_requires=[
    package for package in open('requirements.txt').read().split('\n') if package and package not in ignore_packages
  ],
  author='roysatadru',
  description='Utility Trading Indicators',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/roysatadru/trading_indicators',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.12',
)
