.. _dev_building:

Publishing Contributions
========================

GBasis, like all HORTON 3 modules, has a robust build system included which
builds off the Conda architecture and Travis-CI. This ensures our codebase
meets certain quality standards.

When making a new feature for Gbasis, you should **fork the main repository
and then make a pull request from your fork to the master branch**. The pull
request will then be verified by Travis-CI. Travis checks for several things:

* PEP-8 (code style) compliance
* PEP-257 (docstring) compliance
* Unit tests pass
* Unit testing coverage
* Linux/OSX compatibility

You can examine the Travis-CI error log if your code fails and make the
appropriate changes. Every commit to your pull request will be tested
automatically.

Tips
----

You should check your code before making a pull request to save yourself
some trouble. Using a modern IDE like Pycharm will go a long way to
making sure your code complies with PEP-8, PEP-257, and so forth. Use the
code refactoring features.

You will also find that testing locally can save you some time.
Run nosetests on your own machine before submitting your PR.

Building with Conda on your own machine will emulate lots of the build
tests and give you a virtualenv that will be more reliable.

The instructions for compiling with Conda are listed in
:ref:`install_from_source`. This is the build which will be executed
by Travis-CI when making a pull request.

Introducing new dependencies
----------------------------

Sometimes a contribution will introduce a dependency on another library. This will need to be added
to the conda virtualenv when building the package for testing. This can be done in
``tools/conda.recipe/meta.yaml``. Depending on whether your dependency is a Python library, or a
compiled C/C++ library, it needs to go in different sections.

The ``host`` section is for packages which will be installed into the build environment. This is for
C/C++ dependencies.

.. code-block:: yaml

    host:
    - python ={{ MYCONDAPY }}
    - libint
    - cython >=0.24.1
    - numpy
    - setuptools
    - nose

The ``run`` section is for installing dependencies on the user's machine. This is for Python
dependencies. This is also for libraries which need to be dynamically linked. In theory the Conda
build tools will automatically add the linked libraries from ``host`` here as well, but in practice
the process is not reliable. You are advised to add them in as well.

.. code-block:: yaml

    run:
    - python >=3
    - numpy
    - scipy
    - nose
    - libint

For details on the ``meta.yaml`` file, read the
`conda-build documentation
<https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html>`_.
Some commands within the documentation are incorrect/out-of-date. You have been forewarned...