from setuptools import setup, find_packages
from codecs import open
from os import path
import subprocess
import sys

__version__ = '{{cookiecutter.version}}'

here = path.abspath(path.dirname(__file__))

pandoc_call = ['pandoc', '--from=markdown', '--to=rst', 'README.md']

try:
    output = subprocess.run(pandoc_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if output.returncode:
        print(output.stderr)
        sys.exit()
    output = output.stdout
except AttributeError:
    try:
        output = subprocess.check_output(pandoc_call)
    except subprocess.CalledProcessError:
        sys.exit()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='{{cookiecutter.app_name}}',
    version=__version__,
    description='{{cookiecutter.project_short_description}}',
    long_description=output,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/tarball/' + __version__,
    license='GPLv3',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author='{{cookiecutter.full_name}}',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='{{cookiecutter.email}}'
)
