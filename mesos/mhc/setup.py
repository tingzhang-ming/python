import os
from setuptools import setup, find_packages


COMMONS_VERSION = '==0.3.2'
MESOS_VERSION = '==1.4.0'

here = os.path.abspath(os.path.dirname(__file__))

def make_commons_requirement(name):
  return 'twitter.common.{0}{1}'.format(name, COMMONS_VERSION)


def list_package_data_files(package_root, data_folder):
  """List the data files in the data_folder under the given package_root."""
  paths = []
  for root, _, files in os.walk(os.path.join(package_root, data_folder)):
    for filename in files:
      paths.append(os.path.relpath(os.path.join(root, filename), package_root))

  return paths


setup(
    name='god',
    version='0.0.1',
    description='Mhc test framework',
    url='',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='mesos',
    packages=find_packages(),
    package_data={
        '': (list_package_data_files('god/executor', 'files') +
             list_package_data_files('god/scheduler', 'assets'))
    },
    dependency_links=[
        'packages'
    ],
    install_requires=[
        make_commons_requirement('http'),
        make_commons_requirement('zookeeper'),
        make_commons_requirement('metrics'),
        make_commons_requirement('exceptions'),
        make_commons_requirement('decorators'),
        make_commons_requirement('app'),
        make_commons_requirement('util'),
        make_commons_requirement('contextutil'),
        make_commons_requirement('process'),
        make_commons_requirement('string'),
        make_commons_requirement('collections'),
        make_commons_requirement('quantity'),
        make_commons_requirement('log'),
        make_commons_requirement('options'),
        make_commons_requirement('dirutil'),
        make_commons_requirement('decorators'),
        make_commons_requirement('lang'),
        'PyNaCl==0.3.0',
        'cffi==1.8.3',
        'pycparser==2.09',
        'CherryPy==3.2.2',
        'Mako==0.4.0',
        'bottle==0.11.6',
        'MarkupSafe==0.12',
        'six==1.9',
        'thrift==0.9.1',
        'futures==2.1.6',
        'kazoo==1.3.1',
        'zope.interface==4.2.0',
    ],

    entry_points={
        'console_scripts': [
            'god_scheduler=god.scheduler.god_scheduler:proxy_main',
            # 'god_executor=hyaline.executor.hyaline_executor:proxy_main',
            # 'god_client=hyaline.api.hyaline_client:proxy_main',
        ],
    },
)
