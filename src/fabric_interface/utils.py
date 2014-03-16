__author__ = 'heddevanderheide'

# Django specific
from django.contrib import admin


class StackedInlineWithLimitedManyToManyFields(admin.StackedInline):
    limited_manytomany_fields = {}

    def get_formset(self, request, obj=None, **kwargs):
        self.parent_obj = obj
        return super(StackedInlineWithLimitedManyToManyFields, self).get_formset(request, obj, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in self.limited_manytomany_fields.keys() and hasattr(self, 'parent_obj'):
            kwargs['queryset'] = db_field.rel.to.objects.filter(
                **{
                    self.limited_manytomany_fields[db_field.name]: self.parent_obj
                }
            )
        return super(StackedInlineWithLimitedManyToManyFields, self).formfield_for_manytomany(
            db_field, request, **kwargs
        )
