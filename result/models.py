from django.db import models


class Result(models.Model):
    enroll_id = models.IntegerField(null=True)
    round_one_second = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    round_one_miss_conr = models.IntegerField(null=True)
    round_one_result = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    round_two_second = models.IntegerField(null=True)
    round_two_miss_conr = models.CharField(max_length=2, null=True)
    round_two_result = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    skill_1 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    art_1 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    score_1 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    skill_2 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    art_2 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    score_2 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    skill_3 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    art_3 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    score_3 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    skill_4 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    art_4 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    score_4 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    skill_5 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    art_5 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    score_5 = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    punish = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    final_result = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    rank = models.IntegerField(null=True)
    integral = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'result'
