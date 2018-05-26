# -*- coding: utf-8 -*-

"""A PyBEL extension for interacting with its database through Flask Admin.

Installation
------------
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

Citation
--------
If you use PyBEL in your work, please cite:

.. [1] Hoyt, C. T., *et al.* (2017). `PyBEL: a Computational Framework for Biological Expression Language
       <https://doi.org/10.1093/bioinformatics/btx660>`_. Bioinformatics, 34(December), 1–2.

"""

from . import views
from .admin import build_admin_service
from .application import create_app

__all__ = [
    'create_app',
    'build_admin_service',
    'views',
]

__version__ = '0.0.1-dev'

__title__ = 'pybel_admin'
__description__ = 'A PyBEL extension for interacting with its database through Flask Admin'
__url__ = 'https://github.com/pybel/pybel-admin'

__author__ = 'Charles Tapley Hoyt'
__email__ = 'charles.hoyt@scai.fraunhofer.de'

__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2018 Charles Tapley Hoyt'
