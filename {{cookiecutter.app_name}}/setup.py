from setuptools import setup, find_packages
import codecs
import os
import subprocess
import sys

base_dir = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(base_dir, 'src')
# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)
about = {}
with open(os.path.join(src_dir, '{{cookiecutter.app_name}}', '__about__.py')) as f:
    exec(f.read(), about)


def genRST():
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
    return output

# get the dependencies and installs
with codecs.open(os.path.join(base_dir, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    long_description=genRST(),
    url=about['__uri__'],
    license=about['__license__'],
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author=about['__author__'],
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email=about['__email__']
)
