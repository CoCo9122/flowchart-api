from django.db import models

class Node(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    node = models.TextField(verbose_name='ノードデータ')

class Edge(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    edge = models.TextField(verbose_name='エッジデータ')

class ChartType(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    name = models.CharField(verbose_name='タイプ名', max_length=255)
    img_url = models.TextField(verbose_name='画像URL', null=True, blank=True)