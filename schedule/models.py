from django.db import models


class Schedule(models.Model):
    competition_id = models.IntegerField()
    order = models.CharField(max_length=10, null=True)
    level = models.CharField(max_length=50, null=True)
    group = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    item = models.CharField(max_length=50, null=True)
    competition_type = models.CharField(max_length=20, null=True)
    remark = models.CharField(max_length=50, null=True)
    number_of_player = models.SmallIntegerField()
    competition_day = models.IntegerField(null=True)
    each_group_estimate_second = models.SmallIntegerField(null=True)
    each_time_number_of_player = models.IntegerField(null=True)
    estimate_time = models.DateTimeField(null=True)
    open_result_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schedule'
