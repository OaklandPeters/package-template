from setuptools import setup

# Filling in this template requires filling in:
# name
# description
# packages
# classifiers
#    Development Status :: 
# ... it would also be beneficial to study/fill in other classifiers 
#
# Also will benefit from confirming the url -- which may change frequently
#    ... such as if not using bitbucket


def TEMPLATE(placeholder='unspecified'):
    raise Exception("Template has not yet been filled in: "+unspecified)

setup(
    name=TEMPLATE('{package-name}'),
    version=open('VERSION').read().strip(),
    author='Oakland John Peters',
    author_email='oakland.peters@gmail.com',

    description=TEMPLATE('{long-description'),
    long_description=open('README.rst').read(),
    url=TEMPLATE('package: http://bitbucket.org/OPeters/{package-name}'),
    license='MIT',

    packages=[TEMPLATE('{package-name}')],

    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ]
)
