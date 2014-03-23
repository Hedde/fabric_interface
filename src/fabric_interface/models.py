__author__ = 'heddevanderheide'

# Django specific
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import striptags
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# App specific
from fabric_interface.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        db_index=True,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date created'),
        auto_created=True,
        default=timezone.now
    )

    is_active = models.BooleanField(verbose_name=_(u"Active"), default=True)
    is_admin = models.BooleanField(verbose_name=_(u"Admin"), default=False)

    first_name = models.CharField(verbose_name=_(u"First name"), max_length=125)
    family_name_prefix = models.CharField(verbose_name=_(u"Family name prefix"), max_length=125, blank=True, null=True)
    family_name = models.CharField(verbose_name=_(u"Family name"), max_length=125)

    content_type = models.ForeignKey(ContentType, editable=False, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def get_full_name(self):
        if self.family_name_prefix:
            return '{first_name} {family_name_prefix} {family_name}'.format(
                first_name=self.first_name,
                family_name_prefix=self.family_name_prefix,
                family_name=self.family_name
            )
        return '{first_name} {family_name}'.format(
            first_name=self.first_name,
            family_name=self.family_name
        )

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def as_leaf_class(self):
        "Multi table inheritance helper"
        content_type = self.content_type
        model = content_type.model_class()
        if model == User:
            return self
        return model.objects.get(id=self.id)

    def save(self, *args, **kwargs):
        if not self.content_type:
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        super(User, self).save(*args, **kwargs)

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        # This might be simplified in django 1.7
        text_content = striptags(message)
        html_content = message

        msg = EmailMultiAlternatives(subject, text_content, from_email, [self.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()