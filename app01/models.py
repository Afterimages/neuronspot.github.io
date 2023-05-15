# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ada(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ada = models.CharField(db_column='ADA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'ada'


class Ade(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ade = models.CharField(db_column='ADE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ade'


class Adf(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    adf = models.CharField(db_column='ADF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'adf'


class Adl(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    adl = models.CharField(db_column='ADL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'adl'


class Afd(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    afd = models.CharField(db_column='AFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'afd'


class Aia(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aia = models.CharField(db_column='AIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aia'


class Aib(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aib = models.CharField(db_column='AIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aib'


class Aim(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aim = models.CharField(db_column='AIM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aim'


class Ain(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ain = models.CharField(db_column='AIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ain'


class Aiy(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aiy = models.CharField(db_column='AIY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aiy'


class Aiz(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aiz = models.CharField(db_column='AIZ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aiz'


class Ala(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ala = models.CharField(db_column='ALA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ala'


class Alm(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    alm = models.CharField(db_column='ALM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'alm'


class Aln(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aln = models.CharField(db_column='ALN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aln'


class Aqr(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aqr = models.CharField(db_column='AQR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aqr'


class As(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    as_field = models.CharField(db_column='AS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'as'


class Asel(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    asel = models.CharField(db_column='ASEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asel'


class Aser(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aser = models.CharField(db_column='ASER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aser'


class Asg(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    asg = models.CharField(db_column='ASG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asg'


class Ash(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ash = models.CharField(db_column='ASH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ash'


class Asi(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    asi = models.CharField(db_column='ASI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asi'


class Asj(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    asj = models.CharField(db_column='ASJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asj'


class Ask(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ask = models.CharField(db_column='ASK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ask'


class Aua(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    aua = models.CharField(db_column='AUA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aua'


class Ava(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ava = models.CharField(db_column='AVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ava'


class Avb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avb = models.CharField(db_column='AVB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avb'


class Avd(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avd = models.CharField(db_column='AVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avd'


class Ave(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ave = models.CharField(db_column='AVE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ave'


class Avf(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avf = models.CharField(db_column='AVF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avf'


class Avg(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avg = models.CharField(db_column='AVG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avg'


class Avh(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avh = models.CharField(db_column='AVH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avh'


class Avj(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avj = models.CharField(db_column='AVJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avj'


class Avk(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avk = models.CharField(db_column='AVK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avk'


class Avl(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avl = models.CharField(db_column='AVL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avl'


class Avm(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    avm = models.CharField(db_column='AVM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avm'


class Awa(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    awa = models.CharField(db_column='AWA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'awa'


class Awb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    awb = models.CharField(db_column='AWB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'awb'


class AwcOff(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    awc_off = models.CharField(db_column='AWC_OFF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'awc_off'


class AwcOn(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    awc_on = models.CharField(db_column='AWC_ON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'awc_on'


class Bag(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    bag = models.CharField(db_column='BAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bag'


class Bdu(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    bdu = models.CharField(db_column='BDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bdu'


class Can(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    can = models.CharField(db_column='CAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'can'


class Cep(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(db_column='CEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cep'


class Da(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    da = models.CharField(db_column='DA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'da'


class Da9(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    da9 = models.CharField(db_column='DA9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'da9'


class Db(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    db = models.CharField(db_column='DB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'db'


class Db01(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    db01 = models.CharField(db_column='DB01', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'db01'


class Dva(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    dva = models.CharField(db_column='DVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dva'


class Dvb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    dvb = models.CharField(db_column='DVB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dvb'


class Dvc(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    dvc = models.CharField(db_column='DVC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dvc'


class Flp(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    flp = models.CharField(db_column='FLP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'flp'


class Hsn(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    hsn = models.CharField(db_column='HSN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hsn'


class I1(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    i1 = models.CharField(db_column='I1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'i1'


class I2(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    i2 = models.CharField(db_column='I2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'i2'


class I3(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    i3 = models.CharField(db_column='I3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'i3'


class I4(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    i4 = models.CharField(db_column='I4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'i4'


class I5(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    i5 = models.CharField(db_column='I5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'i5'


class I6(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    i6 = models.CharField(db_column='I6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'i6'


class Il1(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    il1 = models.CharField(db_column='IL1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'il1'


class Il2Dv(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    il2_dv = models.CharField(db_column='IL2_DV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'il2_dv'


class Il2Lr(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    il2_lr = models.CharField(db_column='IL2_LR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'il2_lr'


class Lua(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    lua = models.CharField(db_column='LUA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lua'


class M1(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    m1 = models.CharField(db_column='M1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'm1'


class M2(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    m2 = models.CharField(db_column='M2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'm2'


class M3(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    m3 = models.CharField(db_column='M3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'm3'


class M4(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    m4 = models.CharField(db_column='M4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'm4'


class M5(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    m5 = models.CharField(db_column='M5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'm5'


class Mc(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    mc = models.CharField(db_column='MC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mc'


class Mi(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    mi = models.CharField(db_column='MI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mi'


class Nsm(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    nsm = models.CharField(db_column='NSM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nsm'


class Oll(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    oll = models.CharField(db_column='OLL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'oll'


class Olq(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    olq = models.CharField(db_column='OLQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olq'


class Pda(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pda = models.CharField(db_column='PDA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pda'


class Pdb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pdb = models.CharField(db_column='PDB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdb'


class Pde(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pde = models.CharField(db_column='PDE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pde'


class Pha(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pha = models.CharField(db_column='PHA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pha'


class Phb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    phb = models.CharField(db_column='PHB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phb'


class Phc(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    phc = models.CharField(db_column='PHC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phc'


class Plm(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    plm = models.CharField(db_column='PLM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plm'


class Pln(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pln = models.CharField(db_column='PLN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pln'


class Pqr(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pqr = models.CharField(db_column='PQR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pqr'


class Pvc(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvc = models.CharField(db_column='PVC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvc'


class Pvd(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvd = models.CharField(db_column='PVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvd'


class Pvm(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvm = models.CharField(db_column='PVM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvm'


class Pvn(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvn = models.CharField(db_column='PVN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvn'


class Pvp(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvp = models.CharField(db_column='PVP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvp'


class Pvq(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvq = models.CharField(db_column='PVQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvq'


class Pvr(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvr = models.CharField(db_column='PVR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvr'


class Pvt(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvt = models.CharField(db_column='PVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvt'


class Pvw(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    pvw = models.CharField(db_column='PVW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pvw'


class Ria(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ria = models.CharField(db_column='RIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ria'


class Rib(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rib = models.CharField(db_column='RIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rib'


class Ric(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ric = models.CharField(db_column='RIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ric'


class Rid(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rid = models.CharField(db_column='RID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rid'


class Rif(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rif = models.CharField(db_column='RIF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rif'


class Rig(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rig = models.CharField(db_column='RIG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rig'


class Rih(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rih = models.CharField(db_column='RIH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rih'


class Rim(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rim = models.CharField(db_column='RIM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rim'


class Rip(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rip = models.CharField(db_column='RIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rip'


class Rir(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rir = models.CharField(db_column='RIR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rir'


class Ris(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ris = models.CharField(db_column='RIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ris'


class Riv(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    riv = models.CharField(db_column='RIV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'riv'


class RmdDv(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rmd_dv = models.CharField(db_column='RMD_DV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rmd_dv'


class RmdLr(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rmd_lr = models.CharField(db_column='RMD_LR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rmd_lr'


class RmeDv(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rme_dv = models.CharField(db_column='RME_DV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rme_dv'


class RmeLr(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rme_lr = models.CharField(db_column='RME_LR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rme_lr'


class Rmf(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rmf = models.CharField(db_column='RMF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rmf'


class Rmg(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rmg = models.CharField(db_column='RMG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rmg'


class Rmh(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    rmh = models.CharField(db_column='RMH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rmh'


class Saa(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    saa = models.CharField(db_column='SAA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'saa'


class Sab(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    sab = models.CharField(db_column='SAB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sab'


class Sdq(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    sdq = models.CharField(db_column='SDQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sdq'


class Sia(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    sia = models.CharField(db_column='SIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sia'


class Sib(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    sib = models.CharField(db_column='SIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sib'


class Smb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    smb = models.CharField(db_column='SMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'smb'


class Smd(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    smd = models.CharField(db_column='SMD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'smd'


class Ura(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ura = models.CharField(db_column='URA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ura'


class Urb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    urb = models.CharField(db_column='URB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'urb'


class Urx(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    urx = models.CharField(db_column='URX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'urx'


class Ury(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    ury = models.CharField(db_column='URY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ury'


class Va(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    va = models.CharField(db_column='VA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'va'


class Va12(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    va12 = models.CharField(db_column='VA12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'va12'


class Vb(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    vb = models.CharField(db_column='VB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vb'


class Vb01(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    vb01 = models.CharField(db_column='VB01', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vb01'


class Vb02(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    vb02 = models.CharField(db_column='VB02', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vb02'


class Vc(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    vc = models.CharField(db_column='VC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vc'


class Vc45(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    vc_4_5 = models.CharField(db_column='VC_4_5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vc_4_5'


class VdDd(models.Model):
    gene_name = models.CharField(max_length=255, blank=True, null=True)
    vd_dd = models.CharField(db_column='VD_DD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    extra_count = models.CharField(max_length=255, blank=True, null=True)
    primary_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vd_dd'
