from django.db import models





class Competition(models.Model):
    name = models.CharField(max_length=50, null=True)
    letter = models.JSONField(null=True)
    location = models.CharField(max_length=100, null=True)
    start_time = models.DateTimeField(null=True)
    date = models.DateTimeField(null=True)
    is_integral = models.IntegerField(null=True)
    is_open_enroll = models.IntegerField(null=True)
    is_open_edit = models.IntegerField(null=True)
    is_open_document = models.IntegerField(null=True)
    is_open_estimate = models.IntegerField(null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'competition'

    def get_comptition(request):
        return Competition.objects.all()