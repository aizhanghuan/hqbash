from django.db import models

# Create your models here.
class TUser(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_user'




class TLog(models.Model):
    id = models.IntegerField(primary_key=True)
    port = models.CharField(max_length=33, blank=True, null=True)
    cookie = models.CharField(max_length=33, blank=True, null=True)
    revision = models.CharField(max_length=33, blank=True, null=True)
    url = models.CharField(max_length=11, blank=True, null=True)
    yu1 = models.CharField(max_length=11, blank=True, null=True)
    yu2 = models.CharField(max_length=11, blank=True, null=True)
    yu3 = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_log'







class Text(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=222, blank=True, null=True)
    sex = models.CharField(max_length=222, blank=True, null=True)
    marry = models.CharField(max_length=222, blank=True, null=True)
    age = models.CharField(max_length=222, blank=True, null=True)
    birth = models.CharField(max_length=222, blank=True, null=True)
    xuewei = models.CharField(max_length=222, blank=True, null=True)
    country = models.CharField(max_length=222, blank=True, null=True)
    qunti = models.CharField(max_length=225, blank=True, null=True)
    qiuzhistate = models.CharField(max_length=225, blank=True, null=True)
    qiwaddr = models.CharField(max_length=222, blank=True, null=True)
    qiwzhiwei = models.CharField(max_length=222, blank=True, null=True)
    gongzuoxingzhi = models.CharField(max_length=222, blank=True, null=True)
    qiwanghangye = models.CharField(max_length=222, blank=True, null=True)
    qiwangsalary = models.CharField(max_length=222, blank=True, null=True)
    jiaoyutime = models.CharField(max_length=222, blank=True, null=True)
    xueyuan = models.CharField(max_length=222, blank=True, null=True)
    language = models.CharField(max_length=222, blank=True, null=True)
    xueli = models.CharField(max_length=222, blank=True, null=True)
    daogshijian = models.CharField(max_length=222, blank=True, null=True)
    experence = models.CharField(max_length=222, blank=True, null=True)
    number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'text'

