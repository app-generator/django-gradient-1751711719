# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Holding_Companies(models.Model):

    #__Holding_Companies_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    nama_holding = models.CharField(max_length=255, null=True, blank=True)
    email_kontak = models.CharField(max_length=255, null=True, blank=True)
    alamat = models.TextField(max_length=255, null=True, blank=True)
    telepon = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    tanggal_bergabung = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Holding_Companies_FIELDS__END

    class Meta:
        verbose_name        = _("Holding_Companies")
        verbose_name_plural = _("Holding_Companies")


class Tenants(models.Model):

    #__Tenants_FIELDS__
    nama_perusahaan = models.CharField(max_length=255, null=True, blank=True)
    email_kontak = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True)
    status_aktif = models.BooleanField()
    tanggal_daftar = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Tenants_FIELDS__END

    class Meta:
        verbose_name        = _("Tenants")
        verbose_name_plural = _("Tenants")


class Pengguna(models.Model):

    #__Pengguna_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    password_hash = models.TextField(max_length=255, null=True, blank=True)
    jabatan = models.CharField(max_length=255, null=True, blank=True)

    #__Pengguna_FIELDS__END

    class Meta:
        verbose_name        = _("Pengguna")
        verbose_name_plural = _("Pengguna")



#__MODELS__END
