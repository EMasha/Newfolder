# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.gis.db import models


# Create your models here.
class lloji (models.Model):
    lloji = models.CharField(max_length=250)

    def __str__(self):
        return self.lloji

class biznes (models.Model):
    biznes = models.CharField(max_length=250)

    def __str__(self):
        return self.biznes

class status (models.Model):
    status = models.CharField(max_length=250)

    def __str__(self):
        return self.status

class qytet (models.Model):
    qytet = models.CharField(max_length=250)

    def __str__(self):
        return self.qytet

class rruget (models.Model):
    emri = models.CharField(max_length=250)

    def __unicode__(self):
        return self.emri

class zona (models.Model):
    zona = models.CharField(max_length=250)
    id_qytet = models.ForeignKey(qytet, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.zona

class vendodhje (models.Model):
    id_rruga = models.ForeignKey(rruget, on_delete=models.CASCADE)
    id_zona = models.ForeignKey(zona, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s - %s' % (self.id_rruga, self.id_zona)




class prona (models.Model):
    id_vendodhje = models.ForeignKey(vendodhje, default='',on_delete=models.CASCADE)
    id_lloji = models.ForeignKey(lloji, default='',on_delete=models.CASCADE)
    cmimi = models.IntegerField()
    dhoma = models.IntegerField()
    banjo = models.IntegerField()
    size = models.IntegerField()
    titulli = models.CharField(max_length=250)
    pershkrim = models.CharField(max_length=1000)
    id_biznes = models.ForeignKey(biznes, default='',on_delete=models.CASCADE)
    status = models.IntegerField()
    geom = models.PointField()
    url = models.CharField(max_length=100)
    hits = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(default=datetime.datetime.now)
    modif_date = models.DateField(default=datetime.datetime.now)
    sponsorizuar = models.IntegerField()
    objects = models.GeoManager()

    def get_absolute_url(self):
        return reverse('prona:prona_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.titulli


class atributi (models.Model):
    id_prona = models.ForeignKey(prona, on_delete=models.CASCADE)
    atributi = models.CharField(max_length=250)
    vlera = models.CharField(max_length=250)

class foto (models.Model):
    url = models.CharField(max_length=200)
    id_prona = models.ForeignKey(prona, on_delete=models.CASCADE)
    kryesore = models.IntegerField()