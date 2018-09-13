# -*- coding: utf-8 -*-

"""PyBEL-Admin command line interface.

PyBEL-Admin installs a command ``pybel-admin`` that can be directly called from the console. Alternatively, it can
be run as a Python module with:

.. code-block:: sh

    $ python3 -m pybel_admin

The options ``--host`` and ``--port`` can be used to change these default parameters from ``localhost`` and ``5000``,
respectively.

"""

import sys

import click

from pybel.constants import get_cache_connection
from .application import create_app


@click.command(help="PyBEL Admin on {} using default connection {}".format(sys.executable, get_cache_connection()))
@click.option('-c', '--connection')
@click.option('-h', '--host')
@click.option('-p', '--port', type=int)
def main(connection, host, port):
    """Run PyBEL Flask Admin."""
    app = create_app(manager=connection)
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
