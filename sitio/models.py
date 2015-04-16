from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    about_me = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{}'s profile'".format(self.user.username)

    class Meta:
        db_table = 'user_profile'


    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
