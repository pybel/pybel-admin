PyBEL-Admin |build| |coverage| |documentation|
==============================================
A PyBEL extension for interacting with its database through Flask Admin.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
Get the Latest
~~~~~~~~~~~~~~~
Download the most recent code from `GitHub <https://github.com/pybel/pybel-admin>`_ with:

.. code-block:: sh

   $ python3 -m pip install git+https://github.com/pybel/pybel-admin.git

For Developers
~~~~~~~~~~~~~~
Clone the repository from `GitHub <https://github.com/pybel/pybel-admin>`_ and install in editable mode with:

.. code-block:: sh

   $ git clone https://github.com/pybel/pybel-admin.git
   $ cd bio2bel
   $ python3 -m pip install -e .

Getting Started
---------------
PyBEL-Admin installs a command ``pybel-admin`` that can be directly called from the console. Alternatively, it can
be run as a Python module with:

.. code-block:: sh

    $ python3 -m pybel_admin

The options ``--host`` and ``--port`` can be used to change these default parameters from ``localhost`` and ``5000``,
respectively.

Citation
--------
If you use PyBEL in your work, please cite:

.. [1] Hoyt, C. T., *et al.* (2017). `PyBEL: a Computational Framework for Biological Expression Language
       <https://doi.org/10.1093/bioinformatics/btx660>`_. Bioinformatics, 34(December), 1–2.


.. |build| image:: https://travis-ci.org/pybel/pybel-admin.svg?branch=master
    :target: https://travis-ci.org/pybel/pybel-admin
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/pybel/pybel-admin/coverage.svg?branch=master
    :target: https://codecov.io/gh/pybel/pybel-admin?branch=master
    :alt: Coverage Status

.. |documentation| image:: https://readthedocs.org/projects/mirtarbase/badge/?version=latest
    :target: http://mirtarbase.readthedocs.io
    :alt: Documentation Status

.. |climate| image:: https://codeclimate.com/github/pybel/pybel-admin/badges/gpa.svg
    :target: https://codeclimate.com/github/pybel/pybel-admin
    :alt: Code Climate

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/pybel-admin.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/pybel-admin.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pybel-admin.svg
    :alt: MIT License
