import os

from setuptools import find_packages
from setuptools import setup


version = '4.0'


install_requires = [
    'Chameleon >= 2.10',
    'grokcore.component',
    'grokcore.view',
    'setuptools',
    'z3c.pt >= 2.2.2',
    'zope.i18n',
]


tests_require = [
    'grokcore.viewlet',
    'zope.app.appsetup',
    'zope.app.wsgi',
    'zope.testbrowser',
    'zope.testrunner',
]


long_description = (
    open('README.rst').read() +
    '\n\n' +
    open(os.path.join('src', 'grokcore', 'chameleon', 'README.rst')).read() +
    '\n\n' +
    open('CHANGES.rst').read())


setup(
    name='grokcore.chameleon',
    version=version,
    description="Chameleon page template support for Grok",
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope :: 3',
    ],
    keywords="grok chameleon template",
    author="Uli Fouquet",
    author_email="zope-dev@zope.dev",
    url="https://pypi.org/project/grokcore.chameleon/",
    license="ZPL",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['grokcore'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
