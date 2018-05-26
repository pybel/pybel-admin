# -*- coding: utf-8 -*-

"""PyBEL-Admin command line interface.

Run ``pybel-admin`` from the command line to start the Flask Admin view over the PyBEL database. Optionally,
the host and port can be specified.
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
    app = create_app(connection=connection)
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
