"""
    sphinxit.exceptions
    ~~~~~~~~~~~~~~~~~~~

    Implements Sphinxit typical exceptions.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""


class SphinxQLDriverException(Exception):
    pass


class SphinxQLSyntaxException(Exception):
    pass


class ImproperlyConfigured(Exception):
    pass
