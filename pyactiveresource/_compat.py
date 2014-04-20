# -*- coding: utf-8 -*-
"""
stuff taken from from flask._compat

>Some py2/py3 compatibility support based on a stripped down
>version of six so we don't have to depend on a specific version
>of it.

:copyright: (c) 2014 by Armin Ronacher.
:license: BSD, see LICENSE for more details.
"""

import sys

PY2 = sys.version_info[0] == 2
_identity = lambda x: x


if not PY2:
    text_type = str
    string_types = (str,)
    integer_types = (int, )

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    from io import StringIO

    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value

    implements_to_string = _identity

    # url stuff
    import urllib
    urlparse = urllib.parse
    urlerror = urllib.error
    urlrequest = urllib.request

else:
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

    from cStringIO import StringIO

    exec('def reraise(tp, value, tb=None):\n raise tp, value, tb')

    def implements_to_string(cls):
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda x: x.__unicode__().encode('utf-8')
        return cls

    # url stuff
    import urlparse
    import urllib
    import urllib2
    urlerror = urllib2
    urlrequest = urllib2
    urlparse.urlencode = urllib.urlencode
    urlparse.splituser = urllib.splituser
    urlparse.splitpasswd = urllib.splitpasswd
