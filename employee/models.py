from django.db import models
from flow.models import Node, Edge, ChartType

class Employee(models.Model):
    id = models.AutoField(verbose_name='項番', primary_key=True)
    status = models.IntegerField(verbose_name='ステータス')
    number = models.IntegerField(verbose_name='共通社員番号')
    authority = models.IntegerField(verbose_name='権限')
    gmail = models.CharField(verbose_name='メールアドレス', max_length=255)
    name = models.CharField(verbose_name='名前', max_length=255)
    avatar = models.TextField(verbose_name='アバターのURL')

class EmployeeChart(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    status = models.IntegerField(verbose_name='ステータス')
    name = models.CharField(verbose_name='名前', max_length=255, default='無題のフロー')
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.ForeignKey(ChartType, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    edge = models.ForeignKey(Edge, on_delete=models.CASCADE)
    permission = models.IntegerField(verbose_name='他ユーザ権限')
    other_ids = models.TextField(verbose_name='他ユーザID')
    range_permission = models.IntegerField(verbose_name='編集権限範囲')
    created_at = models.CharField(verbose_name='作成日時', max_length=14)
    updated_at = models.CharField(verbose_name='更新日時', max_length=14)
