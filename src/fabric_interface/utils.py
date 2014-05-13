__author__ = 'heddevanderheide'


VIEWSETS_ORDERMAP = {
    'list_view': 1,
    'create_view': 2,
    'detail_view': 3,
    'update_view': 4,
    'delete_view': 5,

    'configuration_create_view': 10,
    'configuration_detail_view': 11,
    'configuration_update_view': 12,
    'configuration_delete_view': 13,

    'stage_create_view': 20,
    'stage_detail_view': 21,
    'stage_update_view': 22,
    'stage_delete_view': 23,
}

"""
Hack to retain proper ordering when plugging
into viewsets, django-viewsets is probably a
bad idea after all, might want to replace it
by an object oriented solution like for instance
the django-rest-framework implements...
"""