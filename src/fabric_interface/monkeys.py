__author__ = 'heddevanderheide'

import six

# Django specific
from django_extensions.db.fields import AutoSlugField


def __init__(self, *args, **kwargs):
    kwargs.setdefault('blank', True)
    kwargs.setdefault('editable', False)

    populate_from = kwargs.pop('populate_from', None)
    # if populate_from is None:
        # raise ValueError("missing 'populate_from' argument")
    # else:
    self._populate_from = populate_from
    self.separator = kwargs.pop('separator', six.u('-'))
    self.overwrite = kwargs.pop('overwrite', False)
    self.allow_duplicates = kwargs.pop('allow_duplicates', False)
    super(AutoSlugField, self).__init__(*args, **kwargs)


AutoSlugField.__init__ = __init__
"""
Unfortunately django-extensions is not entirely compatible
with Django's migrations, so we need some patching code

n.b. this file is imported explicitly from the init file.
"""