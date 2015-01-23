package-tempalte
===================

Synopsis
----------
Collection of template and stub files for Python packages, intended to be tracked as a GIT repository, and served to PyPI.

Motivation
-----------
To save time when setting up a Python package for the first time, and provide reminders for the numerous project metadata and configuration files.


Basic Python Package Structure
---------------------------------
For a simple Python package, tracked with git, and hosted on Github/Bitbucket,
the following structure suffices. Note that the outer directory `myproject/`
contains project metadata, and the inner `myproject/myproject/` is the Python
package itself.

::

    myproject/
        setup.py
        VERSION
        contributors.txt
        README.rst
        .gitignore
        .git/
        myproject/
            __init__.py
            myproject.py
            test_myproject.py


Project Metadata and Configuration
------------------------------------

template.py : template
    Example of a rigorously structured Python module file.

setup.py : template : packaging : setuptools
    Template of a 

README.rst : documentation : hosting
    A quick guide to your project. `README_TEMPLATE.rst` provides a rough overview of major sections. Many code hosting sites (Github, Bitbucket) look for a `README.txt`/`README.rst` file, and displays the contents in the front page of the project. I suggest `ReSTructured text<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.

MANIFEST.in : packaging : setuptools
    Contains a list of non-py files to be included, such as images, data-tables, and documentation. One file per line, as `include {FILENAME}`, . For more details and more advanced commands (such as `recursive-include`), see `distutils <https://docs.python.org/2/distutils/sourcedist.html#principle>`_. For setup.py to collect these, you will need to specify `include_package_data=True` in the `setup()` function. Copy this into the same directory as your setup.py.

.gitignore : git
    Simple list of files for GIT to ignore. Copy this into the root directory of your repository.

.gitignore_long : git
    Much longer list of files for GIT to ignore. If you wish to use this, rename this to `.gitignore`.

LICENSE.txt : legal
    Legal information on whether this software may be redistributed, and if so, under which license. The default license in `package-template` is the `MIT <http://opensource.org/licenses/MIT>`_, which is among the most permissive, as it allows commerical use and modification of the code. Another common license is the `GNU general Public License (GPL)<http://opensource.org/licenses/lgpl-license>`_, which requires that modifications to also be open-sourced. Another common license is `BSD <http://opensource.org/licenses/BSD-3-Clause>`_, which is more permissive than the GPL, but less permissive than the MIT.

VERSION : packaging : setuptools
    Should contain the software version/release numbers, and no other information. I heavily suggest adopting this habit for all packages, no matter how minor. If you're new and familiar with version numbers, `wikipedia <http://en.wikipedia.org/wiki/Software_versioning>`_ is a good place to start.

contributors.txt : legal
    List of authors. Optional information: email addresses, date of first contribution, and/or field of contribution (espcially for larger projects; ex. 'Patch contributors:', 'Interface Designer', etc).


Configuration and IDE Files
------------------------------
Files used to configure IDEs or code-linters, on a per-project basis. The example files have
default/basic settings, which you may (will) want to customize yourself. These are mostly provided
as reminders -- and so you can fork this repo and customize your own versions.

::

    .pylintrc
    .jshintrc
    .project
    .pydevproject



Contributors
-------------
Oakland John Peters <oakland.peters@gmail.com>


License
---------
Available under the ``MIT license <http://opensource.org/licenses/MIT/>``_.

Copyright (c) 2014, Oakland John Peters.

